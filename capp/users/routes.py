from flask import render_template, Blueprint, redirect, flash, url_for, request
from capp.users.forms import RegistrationForm, LoginForm
from capp.models import User
from capp import db, bcrypt
from flask_login import login_user, current_user, logout_user

users=Blueprint('users',__name__)

@users.route('/register', methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
      user_hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
      user = User(username=form.username.data, email=form.email.data, password=user_hashed_password)
      db.session.add(user)
      db.session.commit()
      flash('¡Tu cuenta ha sido creada! ¡Ahora puedes iniciar sesión!', 'success')
      return redirect(url_for('users.login'))
  return render_template('users/register.html', title='register', form=form)

@users.route('/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if current_user.is_authenticated:
        return redirect(url_for('home.home_home'))
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
        login_user(user, remember=form.remember.data)
        next_page = request.args.get('next')
        flash('¡Has iniciado sesión! ¡Ahora puedes empezar a utilizar nuestra aplicación Light Talk!', 'success')
        return redirect(next_page) if next_page else redirect(url_for('home.home_actividades'))
    else:
        flash('No se pudo iniciar sesión. ¡Verifique su correo electrónico y contraseña!', 'danger') 
  return render_template('users/login.html', title='login', form=form)

@users.route('/logout')
def logout():    
    logout_user()
    return redirect(url_for('home.home_home'))