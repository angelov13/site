# Definicio de Aplicaciones de Flask
# Aqui iran todas las aplicaciones

from flask import Flask

# Importo el modulo de configuraciones
from config import Develop

# Creo una nueva app llamada blog
blog = Flask(__name__)

# Configuro mi app para que tome estas configuraciones:
blog.config.from_object(Develop)