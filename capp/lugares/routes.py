from flask import render_template, Blueprint

lugares=Blueprint('lugares',__name__)

@lugares.route('/salamanca')
def lugares_salamanca():
  return render_template('/lugares/salamanca.html')

@lugares.route('/la_alberca')
def lugares_la_alberca():
    return render_template('/lugares/la_alberca.html')

@lugares.route('/salida')
def lugares_salida():
    return render_template('/lugares/salida.html')