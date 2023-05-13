let habilidades = document.querySelector('#habilidades');
let conquistas = document.querySelector('#conquistas');
let page = document.querySelector('#page');








if(page.innerText == habilidades.innerText){

	console.log(opcao.innerText)
	habilidades.classList.add("active");	

} else if(page.innerText == conquistas.innerText){

	console.log(opcao.innerText)
	conquistas.classList.add("active");	

}
