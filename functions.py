# Funciones que interactuan con la base de datos.
#================================================
from models import db, Users, Options, Admin_groups, Admin,Articles,Gallery,Taxonomy

#===============================================================================================================
#
#    Funciones en estado de desarrollo, requieren ser testeadas!
#
#===============================================================================================================






#===========================================================================================================
# Funciones en estado maduro, que devuelven un objeto: flask_sqlalchemy.BaseQuery
# Contienen datos de una o varias tablas, requieren ser iterados(con for) para ser usados
#===========================================================================================================

# Devuelve la tabla completa de los grupos de administradores.
# Como devuelve una objeto flask_sqlalchemy.BaseQuery, requiere ser iterado para ser usado
def getGroupAdmins():
	group_admins = Admin_groups.query.order_by(Admin_groups.id_group)
	return group_admins

#===========================================================================================================
# Funciones en estado maduro, que no devuelven una tupla(array) ni objeto
#===========================================================================================================

def printData(x):
	print("================================\n\n{}\n\n================================\n".format(x))
	return 0

#===========================================================================================================
# Funciones en estado maduro, que devuelven una tupla(array)
# ==========================================================================================================

# Devuelve una tupla(array) de todos los estados existentes en los Administradores
def getStatesAdmins():
	states = db.session.query(Admin.state_admin).all()
	lista = []
	for state in states:
		if state.state_admin not in lista:
			lista.append(state.state_admin)
	return lista

#===========================================================================================================
# Funciones en estado maduro, devuelven un objeto con propiedades listo para usarse en la vista o template.
#===========================================================================================================

# Devuelve un objeto site, con las propiedades del sitio.
def getInfoSite():
	class site():
		name = Options.query.filter_by(name_option='name').first().value_option
		url = Options.query.filter_by(name_option='url').first().value_option
		charset = Options.query.filter_by(name_option='charset').first().value_option
		author = Options.query.filter_by(name_option='author').first().value_option
		lang = Options.query.filter_by(name_option='lang').first().value_option
		country = Options.query.filter_by(name_option='country').first().value_option
	return site

# Devuelve un objeto error, su uso debe ser unicamente para errores: 400-500
def getErrorInfo(e):
	if e.code == 400 or e.code == 403 or e.code == 404 or e.code == 410 or e.code == 500:
		error_code = Options.query.filter_by(name_option='error_{}'.format(e.code)).first().value_option
		error_info = Options.query.filter_by(name_option='info_{}'.format(e.code)).first().value_option
	else:
		error_info = 'Error Desconocido'
		error_code = e
	class error():
		title = error_code
		description = error_info
		type_page = 'error'
	return error

# Devuelve un objeto con la información de las redes sociales
def getSocial():
	class social():
		id_facebook = Options.query.filter_by(name_option='id_facebook').first().value_option
		facebook = Options.query.filter_by(name_option='facebook').first().value_option
		twitter_user = Options.query.filter_by(name_option='twitter_user').first().value_option
		twitter = Options.query.filter_by(name_option='twitter').first().value_option
		google = Options.query.filter_by(name_option='google').first().value_option
		youtube = Options.query.filter_by(name_option='youtube').first().value_option
	return social