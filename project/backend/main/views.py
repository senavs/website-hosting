from flask import make_response, render_template, url_for, abort, redirect


# create your views funcs/classes here
def home():
    return render_template('home.html')
