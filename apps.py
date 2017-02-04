# Definicio de Aplicaciones de Flask
# Aqui iran todas las aplicaciones
# ====================================
from flask import Flask

# Creo una nueva app llamada blog
blog = Flask(__name__)

# Importo del modulo de configuraciones la app de Blog
from configs import BlogDev,BlogProduction

# Configuro mi app para que tome estas configuraciones:
blog.config.from_object(BlogDev)

#Importando las vistas !importante
import views
