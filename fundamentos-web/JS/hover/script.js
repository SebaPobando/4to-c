let nameTag = document.querySelector("#name-tag");
let nameInput = document.querySelector("#nameInput");

nameInput.addEventListener("input", function () {
    cambiarNombre(this.value);
});

function cambiarNombre(nombre) {
    nameTag.innerText = nombre;
}