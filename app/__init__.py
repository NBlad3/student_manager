import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://{os.getenv('USER')}:{os.getenv('PASSWORD')}@{os.getenv('SERVER')}/{os.getenv('DATABASE')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
from app.models import Dog, Cat

with app.app_context():
    db.create_all()
    print("Database created successfully")
