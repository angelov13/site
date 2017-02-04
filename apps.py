# Nueva Instancia de Flask llamada blog
from flask import Flask
blog = Flask(__name__)

#from configs import BlogProduction
#blog.config.from_object(BlogProduction)

from configs import BlogDev
blog.config.from_object(BlogDev)

from models import db
from models import

import views


# Iniciando Servidor
if __name__=='__main__':
	db.init_app(blog)
	with blog.app_context():
		db.create_all(blog)
	blog.run(port=BlogDev.PORT)
	#blog.run(port=BlogProduction.PORT)