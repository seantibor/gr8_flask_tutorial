# A very simple Flask Hello World app for you to get started with...

from flask import render_template #remove Flask
from app import app # add this line
import random

students = ['Alison','George', 'Jonah','Jake','Peter','Tyler','Savannah','Aviah','Taylor','Ellie','Shaun','Aiden']

# delete app = Flask(__name__) from line 9

@app.route('/')
def hello_world():
    student = random.choice(students)
    return render_template("home.html", student=student)