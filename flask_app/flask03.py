# FLASK Tutorial 1 -- We show ithe bare bones code to get an app up and running

import os                # os is used to get environment variables IP & PORT
from flask import Flask   # Flask is the web app that we will customize
from flask import render_template
from flask import request
app = Flask(__name__)     # create an app
notes = {1: {'title': 'First note', 'text': 'This is my first note', 'date': '10-1-2020'},
            2: {'title': 'Second note', 'text': 'This is my second note', 'date': '10-2-2020'},
            3: {'title': 'Third note', 'text': 'This is my third note', 'date': '10-3-2020'}
             }
# @app.route is a decorator. It gives the function "index" special powers.
# In this case it makes it so anyone going to "your-url/" makes this function
# get called. What it returns is what is shown as the web page
@app.route('/index')
def index():
    a_user = {'name': 'Ted', 'email': 'esalmon1@uncc.edu'}
    return render_template('index.html', user=a_user)

@app.route('/notes')
def get_notes():
    a_user = {'name': 'Ted', 'email': 'esalmon1@uncc.edu'}
    return render_template('notes.html', notes=notes, user=a_user)

@app.route('/notes/<note_id>')
def get_note(note_id):
        a_user = {'name': 'Ted', 'email': 'esalmon1@uncc.edu'}
        return render_template('note.html', note=notes[int(note_id)], user=a_user)

@app.route('/notes/new', methods=['GET', 'POST'])
def new_note():
    a_user = {'name': 'Mogil', 'email': 'mogil@uncc.edu'}

    #check method used for request
    print('request method is', request.method)
    if request.method == 'POST':
        request_data = request.form

        return f"data: {request_data} !"
    else:
        return render_template('new.html', user=a_user)


    return render_template('new.html', user=a_user)


