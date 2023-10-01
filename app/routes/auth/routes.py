from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user
from . import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    # TODO: Handle login logic
    return render_template('login.html')


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
