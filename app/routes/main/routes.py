from flask import render_template, flash, redirect, url_for
from flask_login import login_required
from . import main

@main.route('/')
def index():
    return "Hello from Main Blueprint!"


@main.route('/protected')
@login_required
def protected():
    return render_template('protected.html')
