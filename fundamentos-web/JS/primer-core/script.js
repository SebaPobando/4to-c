let boton = document.getElementById("login-button");

boton.addEventListener("click", function () {
    this.innerText = "Cerrar sesión";
});

let perfil = document.getElementById("profile-button");

perfil.addEventListener("click", function () {
    alert("Estás viendo el perfil");
});

let likeButtons = document.querySelectorAll('.like-btn');
likeButtons.forEach(function (btn) {
    btn.addEventListener('click', function () {
        let texto = this.innerText;
        let partes = texto.split(' ');
        let likes = parseInt(partes[0]);
        likes++;
        this.innerText = likes + ' Me gusta';
    });
});

// profe tonoto xd ekisde lol