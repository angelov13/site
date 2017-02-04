# Importando app 
from app import blog


# Landing Page
@blog.route('/')
def index():
	return "Hello World"

#=============================#
# 		ERRORES DE SERVIDOR			#
#=============================#

@blog.errorhandler(404)
def error(e):
	return 'error 404',404