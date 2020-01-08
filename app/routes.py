# A very simple Flask Hello World app for you to get started with...

from flask import render_template
from app import app
import random

students = ['Alison','George', 'Jonah','Jake','Peter','Tyler','Savannah','Aviah','Taylor','Ellie','Shaun','Aiden']

@app.route('/')
@app.route('/hello')
def hello_world():
    student = random.choice(students)
    return render_template("home.html", student=student, teacher='Mr. Tibor')

@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/banana')
def banana():
    return "Why do you want a banana? (Bananananananaa)"