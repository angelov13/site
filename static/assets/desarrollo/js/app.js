var toggleMenu = document.getElementById('toggle-menu');
var menu = document.getElementById('menu');
function mostrar(){
	menu.classList.toggle('mostrar');
}
toggleMenu.addEventListener('click', mostrar, false);