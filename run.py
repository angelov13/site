# Importando blog para Iniciarlo
from blog.app import blog
from config import Develop

import blog.views
if __name__=='__main__':
	blog.run()