# Importando app !importante
from apps import blog

# Importando Modulos Necesarios !importante
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request
from flask import g
from flask import abort
from flask import send_from_directory
from models import db, Users

#=====================================
#		RUTAS DEL SERVIDOR	
#=====================================

@blog.route('/')
def blog():
	pass


#=============================
# 	Archivos estaticos
#=============================

@blog.route('/robots.txt')
def robots():
	return send_from_directory(blog.static_folder,'robots.txt')


#=============================
# 		ERRORES DE SERVIDOR	
#=============================

@blog.errorhandler(403)
def error403(e):
	return render_template('errores/403.html'), 403

@blog.errorhandler(404)
def error404(e):
	return render_template('errores/404.html'), 404

@blog.errorhandler(410)
def error410(e):
	return render_template('errores/410.html'), 410

@blog.errorhandler(500)
def error500(e):
	return render_template('errores/500.html'), 500