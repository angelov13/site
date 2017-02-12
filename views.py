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

from functions import *

#=====================================
#		RUTAS DEL SERVIDOR	
#=====================================

@blog.route('/hack', methods = ['GET'])
def index():
	g.site = getInfoSite()
	g.admin_groups = getGroupAdmins()
	g.states = getStatesAdmins()
	g.page = {
		'title': 'Escritorio'
	}
	return render_template('admin/dashboard.html')


@blog.route('/hack/admin/add',methods = ['GET','POST'])
def adminAdd():
	if request.method == 'POST':
		user=request.form
		nick_name = str(user.get('nick_name'))
		name = str(user.get('name'))
		last_name = str(user.get('last_name'))
		email = str(user.get('email'))
		password = str(user.get('password'))
		state = str(user.get('state'))
		id_group = str(user.get('admin_group'))

		new_admin = Admin(nick_name,name,last_name,email,password,state,id_group)

		db.session.add(new_admin)
		db.session.commit()
	return redirect('/hack')


#=============================
# 	Secciones Temporales
#=============================

@blog.route('/config/<string:option>/<path:value>')
def config(option,value):
	if option == 'install' and value == 'all':
		list_op = {
			'name' : 'Luna Programmers',
			'url' : 'http://lunaprogrammers.com',
			'author' : 'Luna Programmers',
			'lang' : 'es',
			'country' : 'Honduras',
			'charset' : 'utf-8',
			'facebook' : 'https://www.facebook.com/lunaprogrammers',
			'twitter' : 'https://twitter.com/LunaProgrammers',
			'google' : 'https://plus.google.com/u/1/105141538386935423425',
			'youtube' : 'https://www.youtube.com/channel/UCTdEQ-V0Wirwhlp8dYQo6sw',
			'id_facebook' : '1670551139937221',
			'twitter_user' : '@LunaProgrammers',
			'info_400' : 'La Solicitud no pudo realizarse correctamente',
			'info_403' : 'No tienes permisos para estar aquí',
			'info_404' : 'Esta página no existe',
			'info_410' : 'Esta página ya no esta disponible',
			'info_500' : 'Error en servidor, intentelo nuevamente mas tarde',
			'error_400' : '400: Bad Request',
			'error_403' : 'MR. ROBOT',
			'error_404' : '404: Page not Found',
			'error_410' : '410: Page not available',
			'error_500' : '500: Server error',
		}

		def __install__(**kwargs):
			for k,v in kwargs.items():
				x = Options(k,v)
				db.session.add(x)
			db.session.commit()

		__install__(**list_op)

		return 'Instalación realizada Correctamente'
	else:
		op = Options(option,value)
		db.session.add(op)
		db.session.commit()
		return 'Configuración guardada correctamente'

#=================================
#         Redirecciones
#=================================

@blog.route('/administration/')
@blog.route('/administration')
@blog.route('/administrator/')
@blog.route('/administrator')
@blog.route('/dashboard/')
@blog.route('/dashboard')
@blog.route('/wp-admin/')
@blog.route('/wp-admin')
@blog.route('/admin/')
@blog.route('/admin')
def admin():
	abort(403)
	return 403


#==================================
#   Sirviendo Archivos estaticos
#==================================

@blog.route('/robots.txt')
def robots():
	return send_from_directory(blog.static_folder,'robots.txt')


#==================================
#       ERRORES DE SERVIDOR
#==================================

@blog.errorhandler(400)
@blog.errorhandler(403)
@blog.errorhandler(404)
@blog.errorhandler(410)
@blog.errorhandler(500)
def error(e):
	g.site = getInfoSite()
	g.page = getErrorInfo(e)
	return render_template('errores/400-500.html')