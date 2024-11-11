from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userName = request.form.get('userName')
        password = request.form.get('password')

        if not userName or not password:
            flash('Both fields are required.', category='error')
            return render_template("login.html", user=current_user)
        else:
            user = User.query.filter_by(userName=userName).first()

            if user:
                if userName == 'admin':
                    if check_password_hash(user.password, password):
                        login_user(user, remember=True)
                        return redirect(url_for('views.admin'))
                    else:
                        flash('Incorrect password, try again.', category='error')
                elif check_password_hash(user.password, password):
                    login_user(user, remember=True)
                    return redirect(url_for('views.user'))
                else:
                    flash('Incorrect password, try again.', category='error')
            else:
                flash('Username does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/signUp', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        userName = request.form.get('userName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if not userName or not password1 or not password2:
            flash('All fields are required.', category='error')
            return render_template("signUp.html", user=current_user)
        else:
            user = User.query.filter_by(userName=userName).first()
            if user:
                flash('Username already exists.', category='error')
            elif password1 != password2:
                flash('Passwords don\'t match.', category='error')
            else:
                new_user = User(userName=userName, password=generate_password_hash(
                            password1, method='sha256'))
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)
                return redirect(url_for('views.user'))

    return render_template("signUp.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
