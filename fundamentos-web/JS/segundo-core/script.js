// Selecciona todos los botones con la clase 'like-btn'
let likeButtons = document.querySelectorAll('.like-btn');

// Para cada botón encontrado...
likeButtons.forEach(btn => {
    // Asigna una función al evento 'onclick' de cada botón
    btn.onclick = () => {
        // Busca el elemento que muestra los likes dentro del mismo contenedor
        const p = btn.parentElement.querySelector('.like-parrafo');
        // Convierte el texto actual a número (o 0 si no es válido)
        let n = parseInt(p.innerText) || 0;
        // Actualiza el texto con el nuevo número de likes
        p.innerText = (n + 1) + ' like(s)';
    };
});