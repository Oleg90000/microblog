import sqlalchemy as sa 
import sqlalchemy.orm as so
from app import app, db, mail
from app.models import User, Post
from flask_mail import Message

@app.shell_context_processor
def make_shell_context():
    return {
        'sa': sa, 
        'so': so, 
        'db': db, 
        'User': User, 
        'Post': Post, 
        'mail': mail,
        'Message': Message
        }

    