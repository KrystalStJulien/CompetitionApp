from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Krystal' } # fake user
    return render_template("index.html",
        title = 'Home',
        user = user)

@app.route('/new_competition')
def new_comp():
    return render_template("new_comp.html")

@app.route('/profile')
def profile():
    return render_template("profile.html")

@app.route('/points')
def points():
    return render_template("points.html")