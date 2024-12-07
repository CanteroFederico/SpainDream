from flask import render_template, Blueprint

home=Blueprint('home',__name__)

@home.route('/')
@home.route('/home')
def home_home():
  return render_template('home.html')

@home.route('/eventos')
def home_eventos():
  return render_template('eventos.html')

@home.route('/actividades')
def home_actividades():
  return render_template('actividades.html')

@home.route('/equipo')
def home_equipo():
  return render_template('equipo.html')

@home.route('/pruebas')
def home_pruebas():
  return render_template('pruebas.html')