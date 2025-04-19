function mostrarPass() {
    var senha = document.getElementById("inpass");

    if (senha.type === "password") {
        senha.type = "text"; 
    } else {
        senha.type = "password"; 
    }
}