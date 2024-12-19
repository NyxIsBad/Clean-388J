
## CMSC 388J Final Project Proposal

**Group Members (1-4 members):**


```
Select your group members in gradescope!!!
```

**Directions:**

Read the project specifications and fill out all the questions **in gradescope!**

> [!IMPORTANT]
> All the answers to the questions should be submitted to the gradescope submission with all
> of your group members selected


## Logistics

There are 4 things you will submit for the final project (only 1 group member has to submit, but select all members names in gradescope):

1. Proposal
2. Project code
3. Writeup (submit when you submit your project’s code)
4. Adding Styles (Extra credit due at the end of the semester)


Both the Proposal and Writeup use this document as a template (your writeup will likely be the same or similar to your proposal depending on how much has changed since your proposal document).

**Due dates (unless specified elsewhere):**

Proposal: Nov 15, 2024

* We **highly recommend** you complete this as early as possible so you have more time to work on the project. We will review your proposal within 1-2 days of submission.

## Overview

The final project for this class is to create a Flask app in a group of 1-4. You have a lot of freedom for this project as long as you meet the requirements. 

**You’re welcome to use Project 4 (or any other project from this course) as a base (though you’re not required to–in fact, we encourage you to try creating something from scratch)**. *If you choose to use a course project, you need to make a “substantial” change. Examples of “substantial” changes include:*

* Using a different API (instead of the OMDB API) + minor feature to demonstrate knowledge of Flask
* It’s no longer a “review site” but something else
* It’s still a “review site” but you add a major feature
* Examples: ability to reply to reviews

Use your best judgment here but reach out to course instructors if you’re unsure. 

```
Description of your final project idea:

I made a recipe tracker website where users can create a login, create, view, and delete recipes. Users can add new recipes that have details eg. images, ingredients, instructions, and manage their own recipes. Search bar and home page with recommended recipes are open to the public. MongoDB used to store user login data, recipes, etc. Logins are email verified with Flask-Mail.
```



## Requirements

Note that some of these requirements overlap with each other so some features may satisfy multiple requirements.  

**Registration and Login:**



* There needs to be some sort of user control: logging in, registering, logging out.
* Certain features should only be available to logged-in users.

```
Describe what functionality will only be available to logged-in users:
Writing recipes, deleting recipes, their user panel (update username, pfp)
```



**Forms:**



* At least 4 forms (can include registration and login forms)

```
List and describe at least 4 forms:
- Search, sends a query to db
- Registration, creates a new user entry and does email validation
- Login, logs in and sets user
- Update Username - what you'd expect
- Update Profile Picture - same
- Recipe, create a new recipe
- DeleteRecipe, delete a recipe
```



**Blueprints:**



* Must have at least 2 blueprints 
* Each blueprint should have at least 2 visible and accessible routes

```
List and describe your routes/blueprints (don't need to list all routes/blueprints you may have–just enough for the requirement):
- Users
    - contains register, verify email, login, logout, account, user details (so you can view other people's recipes)
- Recipes
    - contains index, search results, recipe, create recipe, delete recipe
```



**Database:**



* Must use MongoDB

```
Describe what will be stored/retrieved from MongoDB:
- Recipes themselves in their entirety
    - eg title, description, ingredients, instructions, image, date posted, author
- User info
    - username, pw, profile picture, email validation details
```



**Another Python Package or API:**



* Find and use another Python package or API.
* Must be a package/API we haven’t used in any of the projects (though anything mentioned in lecture material that wasn’t used in a project is fair game).
* You can use a package/API we’ve already used if you’re using it in a way that’s _very_ different from how we used it in the projects.
* Must affect the user experience in some way.

Examples (feel free to use these or come up with your own):



* Flask-Mail to send emails to users
* CalorieNinjas API with Requests package to access the API
* Spotify API
* Requests package to display data retrieved from an HTTP request
* BeautifulSoup4 to display data parsed from a website
* SciPy, NumPy, SymPy, etc
* Plotly  
* Discord OAuth
* CAS 

```
Describe what Python package or API you will use and how it will affect the user experience:
Flask Mail is used to send verification emails to the user upon registration. It is required to verify in order to post.
```

> [!NOTE]
> Alternatively, you can use your Flask application as a server, and use it as a JSON API for your frontend, a separate app, not using Jinja templating. That will also count for this section.

**Presentation:**

* The website must be hosted and useable.

## Styling (Extra Credit):
> [!IMPORTANT]
> You can earn up to 100pts of "make-up" credit with this, in case you miss any points from the rubric.

Every page of the application must be styled in a way that looks good according to your own taste, and in a way that improves the readability and accessibility of the content.
 - Sometimes that means showing more information on the page that would've been shown without styling.
     - For example, adding a `display: flex` to a number of elements so that more of them can be accessed without scrolling (don't forget to restrict `max-width` of the container and add a `flex-wrap` property to avoid overflows or elements getting cut-off).
 - Sometimes that means adding some space between existing content so that it is easier to see what's going on and the contents on the page are less cluttered.

This will be graded leniently, based on the amount of perceived effort. The more attention to detail, the closer to 100pts you'll get.

Example from Project 4: 
 - more movies are visible on the page than before
 - the navigation buttons are easier to discern
 - color helps separate action button from navigation buttons
 - clickable elements have `:hover` effects

![image](https://github.com/user-attachments/assets/47bb1f4b-406d-4eae-8e01-e1e6ffd472e1)
![image](https://github.com/user-attachments/assets/8a3c4053-fb4f-4c71-8ef4-8bf18cb51812)

## Grading

<table>
  <tr>
   <td>Requirement
   </td>
   <td>Points
   </td>
  </tr>
  <tr>
   <td>Proposal submitted
   </td>
   <td>100
   </td>
  </tr>
  <tr>
   <td>Writeup submitted (same format as the proposal) 
   </td>
   <td>100
   </td>
  </tr>
  <tr>
   <td>Registration and Login
   </td>
   <td>75
   </td>
  </tr>
  <tr>
   <td>Forms
   </td>
   <td>50
   </td>
  </tr>
  <tr>
   <td>Blueprints
   </td>
   <td>50
   </td>
  </tr>
  <tr>
   <td>Database
   </td>
   <td>50
   </td>
  </tr>
  <tr>
   <td>Another Python package or API
   </td>
   <td>75
   </td>
  </tr>
</table>


Total: 500 points\
EC: will make up any missed 100 points