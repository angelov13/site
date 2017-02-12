# Archivo de Configuraciones

# Configuraciones para Desarrollo
class BlogDev():
	DEBUG = True
	SECRET_KEY = 'secret key'
	PORT = 8000
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:hola@localhost/lunaprogrammers_local'
	SQLALCHEMY_TRACK_MODIFICATIONS = False

# Configuraciones para Producción
class BlogProduction():
	DEBUG = False
	PORT = 80
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:hola@localhost/lunaprogrammers'
	SQLALCHEMY_TRACK_MODIFICATIONS = False