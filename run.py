# Importando blog para Iniciarlo !importante
from apps import blog
# Importando configs
from configs import Develop

# Iniciando Servidor
if __name__=='__main__':
	blog.run(port=Develop.PORT)