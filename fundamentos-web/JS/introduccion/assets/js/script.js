function cambiarTexto() {
    document.getElementById("titulo").innerText = "Has cambiado el texto con JS";
}

let nombre = "Francisco";
let edad = 30;

console.log("¡Hola, " + nombre + "! Tienes " + edad + " años.");
console.log("¡Hola, Francisco! Tienes 30 años.")

let x = 10;
x = x + 20;

x += 20; // x = x + 20

for (let i = 0; i <= 15; i++) {
    console.log(i);
}

let usuarios = ["Ana", "Luis", "María"];

for (let i = 0; i < usuarios.length; i++) {
    console.log("Bienvenido, " + usuarios[i]);
}


let reproduciendo = true;

while (reproduciendo) {
    console.log("La canción sigue sonando...");
    // Simulación de una acción que detendría la reproducción
    reproduciendo = false;
}

let datosPendientes = 5;

while (datosPendientes > 0) {
    console.log("Cargando datos...");
    datosPendientes--;
}

while (true) {
    console.log("Este mensaje nunca dejará de mostrarse.");
}