Este sitio web esta desarrollado en flask, sass y javascript.
Construido desde cero sin frameworks en frontend y solo con flask en backend, es compilado por gulp.


ARQUITECTURA DE CARPETAS DEL SITIO
=============================================

docs				#Documentación del Sitio Web
sitio				#Contiene la configuración y la data del sitio
temp				#Datos Temporales
	logs			#Aqui iran los registros de errores
templates		#Templates HTML
	base 			#Plantillas Base: Listas para heredarse
	plugins		#Trozos de HTML con uns sola función
	sections	#Secciones de las páginas
static			#archivos para servirlos
	assets		#Archivos de Desarrollo
		desarrollo
			sass
			js
		final
			css
			js
			fonts
	uploads		#Archivos Multimedia y Documentos
		archivos
		docs
		imagenes
		pdf
		videos

===============================================

ARCHIVOS IMPORTANTES
===============================================

sitio
	articulos.py 		#Contiene los articulos en un array de json's.
	config.py 			#Contiene la configuración del servidor.
	site.py 				#Contiene la impormación del Sitio Web y autor.
docs
	readme.md 			#Contiene la Documentación del Sitio Web.
temp
	logs						#Contiene archivos de registro(logs) de los visitantes
functions.py 			#Aqui se encuentran Todas las Classes y funciones.
									 Es el "controlador" de la DATA
run.py 						#Script que inicia el servidor.
views.py 					#Contiene las "vistas" del Sitio Web, todas las rutas
									 son declaradas aqui, estas renderizan las "templates".
gulpfile.js 			#Archivo de configuración de Gulp
package.json 			#Contiene la lista de Dependencias de NPM

===============================================


ESTRUCTURA DE TEMPLATE "BASE.HTML"
===============================================
			# Bloques de Contanido
html_atributes
meta
seo
links_header
body_atributes

content

links_footer


NOTAS IMPORTANTES
===============================================
Los archivos de desarrollo estan en la carpeta "static/assets/desarrollo"
Los archivos Sass("static/assets/desarrollo/sass") son compilados y minificados con gulp(gulpfile esta en la carpeta raiz)
El javascript("static/assets/desarrollo/js") es minificado con gulp
Los archivos staticos como imagenes, pdf, documentos y videos se encuentran en "static/uploads"

Los archivos finales esta en "static/assets/final"
Las templates se encuentran en "templates", todas estan escritas en HTML 5

Para arrancar el servidor se ejecuta:
	python3 run.py

El servidor por default esta corriendo en "localhost:8000"
para correr browser sync se deve usar --proxy "localhost:8000"
	browser-sync --proxy "localhost:8000" --files "./**/*.*"
	browser-sync --proxy "localhost:8000" --files "./*.*"

No es necesario si se esta corriendo Gulp
para correr Gulp con Browser-Sync solo se necesita ejecutar:
	gulp
