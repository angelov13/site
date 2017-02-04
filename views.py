# Importando app !importante
from apps import blog

# Importando Modulos Necesarios para la Vista !importante
from flask import render_template
from flask import url_for
#===================================================
# Modulos Propios

#==================================================

#=====================================
#		RUTAS DEL SERVIDOR	
#=====================================

# Landing Page
@blog.route('/')
@blog.route('/home')
@blog.route('/index')
def index():

	return render_template('home.html')

# Feed
@blog.route('/feed')
def feed():
	return 'Este sitio no tiene Feed'

#=============================#
# 		ERRORES DE SERVIDOR			#
#=============================#

@blog.errorhandler(403)
def error403():
	return render_template('errores/403.html',), 403

@blog.errorhandler(404)
def error404():
	return render_template('errores/404.html',), 404

@blog.errorhandler(410)
def error410():
	return render_template('errores/410.html',), 410

@blog.errorhandler(500)
def error500():
	return render_template('errores/500.html',), 500