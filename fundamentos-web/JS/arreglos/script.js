let userData = ["Guido", "van Rossum", "guido@python.org"];

userData.push("Programador");
console.log(userData);

userData.pop();
console.log(userData);

userData.splice(1, 1); // Elimina el segundo elemento
console.log(userData);

let hobbies = ["Fotografía", "Ciclismo"];
let perfilCompleto = userData.concat(hobbies);
console.log(perfilCompleto);

