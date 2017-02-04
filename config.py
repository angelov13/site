# Archivo de Configuraciones

class Config(object):
	SECRET_KEY = 'Blog en Flask'

# Configuraciones para Desarrollo
class Develop(Config):
	DEBUG = True
	PORT = 8000

# Configuraciones para Producción
class Production(Config):
	DEBUG = False
	PORT = 80