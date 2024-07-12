from app import app
from flask import Flask, render_template


# @app.route('/')
# def index():
#     return "first page"

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/predict')
def page1():
    return render_template('predict.html')

@app.route('/profile')
def page2():
    return render_template('profile.html')

