// Seleccionamos el botón por su id
let boton = document.getElementById("cambiarTexto");

// Agregamos un evento 'click' al botón
boton.addEventListener("click", function () {
    // Cambia el texto del botón usando `this`
    this.innerText = "¡Texto cambiado!";
});