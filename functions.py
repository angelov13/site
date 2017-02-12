from models import db, Users, Options

def getInfoSite():
	site = {
		'name' : Options.query.filter_by(name_option='name').first().value_option,
		'url' : Options.query.filter_by(name_option='url').first().value_option,
		'charset' : Options.query.filter_by(name_option='charset').first().value_option,
		'author' : Options.query.filter_by(name_option='author').first().value_option,
		'lang' : Options.query.filter_by(name_option='lang').first().value_option,
		'country' : Options.query.filter_by(name_option='country').first().value_option
	}
	return site

def getSocial():
	social = {
		'id_facebook' : Options.query.filter_by(name_option='id_facebook').first().value_option,
		'facebook' : Options.query.filter_by(name_option='facebook').first().value_option,
		'twitter_user' : Options.query.filter_by(name_option='twitter_user').first().value_option,
		'twitter' : Options.query.filter_by(name_option='twitter').first().value_option,
		'google' : Options.query.filter_by(name_option='google').first().value_option,
		'youtube' : Options.query.filter_by(name_option='youtube').first().value_option
	}
	return social

def getErrorInfo(e):
	if e.code == 400 or e.code == 403 or e.code == 404 or e.code == 410 or e.code == 500:
		error_code = Options.query.filter_by(name_option='error_{}'.format(e.code)).first().value_option
		error_info = Options.query.filter_by(name_option='info_{}'.format(e.code)).first().value_option
	else:
		error_info = 'Error Desconocido'
		error_code = e
	error = {
		'title' : error_code,
		'description' : error_info,
		'type' : 'error'
	}
	return error