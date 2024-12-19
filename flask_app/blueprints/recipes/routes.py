from flask import Blueprint, render_template, url_for, redirect, request
from flask_login import current_user, login_required
from datetime import datetime

from ...forms import SearchForm, RecipeForm, DeleteRecipeForm
from ... import db
from ...models import Recipe, User
from ...utils import get_b64_img

recipes = Blueprint('recipes', __name__)

def get_last_id():
    last_id = Recipe.objects().order_by("-recipe_id").first()
    if last_id is None:
        return 0
    return last_id.recipe_id

def get_first_10():
    if get_last_id() <10:
        return Recipe.objects().order_by("-date_posted")
    return Recipe.objects().order_by("-date_posted")[:10]

# View functions

@recipes.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    recipes = get_first_10()
    if form.validate_on_submit():
        return redirect(url_for('recipes.search_results', query=form.search_query.data))
    return render_template('index.html', form=form, recipes=recipes, get_b64_img=get_b64_img)

@recipes.route('/search_results/<query>')
def search_results(query):
    try: 
        results = Recipe.objects(title__icontains=query)
    except ValueError as e:
        return render_template("query.html", error_msg = str(e))
    return render_template('query.html', results=results, query=query)

@recipes.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    recipe = Recipe.objects(recipe_id=recipe_id).first()
    if recipe is None:
        return render_template('404.html', error="Recipe not found")
    """
    recipe has fields 
    - title (string)
    - description (string)
    - ingredients (string)
    - instructions (string)
    - image (image)
    - date_posted (datetime)
    - author (reference to User)
    """
    form = DeleteRecipeForm()
    return render_template('recipe.html', recipe=recipe, get_b64_img=get_b64_img, form=form)

@recipes.route('/create', methods=['GET', 'POST'])
def create():
    if not current_user.is_authenticated:
        return redirect(url_for('users.login'))
    form = RecipeForm()
    if form.validate_on_submit():
        pic_data = form.image.data 
        if pic_data == None:
            # add default here
            pass 
        try:
            recipe = Recipe(
                recipe_id=get_last_id() + 1,
                title=form.title.data,
                description=form.description.data,
                ingredients=form.ingredients.data,
                instructions=form.instructions.data,
                image=pic_data,
                author=current_user,
                date_posted=datetime.now()
            )
            recipe.save()
            return redirect(url_for('recipes.recipe', recipe_id=recipe.recipe_id))
        except Exception as e:
            print(f"Error creating recipe: {e}")
            return redirect(url_for('recipes.create'))
    return render_template('create.html', form=form)

@recipes.route('/delete_recipe/<recipe_id>', methods=['POST'])
@login_required
def delete_recipe(recipe_id):
    recipe = Recipe.objects(recipe_id=recipe_id).first()
    
    if recipe is None:
        print("Recipe not found.")
        return redirect(url_for('users.user', username=current_user.username))

    # Ensure only the author can delete the recipe
    if recipe.author != current_user:
        print("You are not authorized to delete this recipe.")
        return redirect(url_for('users.user', username=current_user.username))

    try:
        recipe.delete()
        print("Recipe deleted successfully.")
    except Exception as e:
        print(f"Error deleting recipe: {e}")

    return redirect(url_for('users.user', username=current_user.username))