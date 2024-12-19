import io
import base64
from itsdangerous import URLSafeTimedSerializer
from flask import current_app

def get_b64_img(image):
    bytes_im = io.BytesIO(image.read())
    image = base64.b64encode(bytes_im.getvalue()).decode()
    return image

def generate_token(email):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    return serializer.dumps(email, salt='email-confirm')

def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    try:
        email = serializer.loads(token, salt='email-confirm', max_age=expiration)
    except Exception:
        return False
    return email