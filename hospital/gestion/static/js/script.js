function validar(campo, validacion) {
    if (validacion) { campo.css('border-color', 'green') }
    else { campo.css('border-color', 'red') }
}
function mostrarAlerta(titulo, texto) {
    Swal.fire({
        title: titulo,
        text: texto,
        imageUrl: '../img/IMG-20240515-WA0161.jpg',
        imageAlt: "icono-hospital",
        imageHeight: 150
    });
}

$(document).ready(function () {
    $(".texto").keyup(function () {
        let formato = /^[a-zA-Z_ áéíóúÁÉÍÓÚ]{0,60}$/;
        let nombre = $(this).val().replace(/\+/g, '\+');
        validar($(this), formato.test(nombre));
    })
    $(".sin-ce").keyup(function () {
        let formato = /^[a-zA-Z0-9_ áéíóúÁÉÍÓÚ]{0,60}$/;
        let campo = $(this).val().replace(/\+/g, '\+');
        validar($(this), formato.test(campo));
    })
    // Validación del formulario de login.html
    $("#password").keyup(function () {
        validar($(this), $(this).val().length <= 20);
    })
    $("#login").click(function () {
        if ($("#username").val() === "" || $("#password").val() === "") {
            mostrarAlerta(
                "Error al autenticar al usuario",
                "Los campos no pueden quedar vacíos. Por favor, rellene todos los campos"
            );
        }
        else {
            window.location.href = "index.html";
        }
    })
    // Validación del formulario de insertar-paciente.html
    $("#historia").keyup(function () {
        let formato = /^[0-9]{1,6}$/;
        let historia = $(this).val().replace(/\+/g, '\+');
        validar($(this), formato.test(historia));
    })
    $("#edad").keyup(function () {
        let formato = /^[0-9]{1,3}$/;
        let edad = $(this).val().replace(/\+/g, '\+');
        let rangoEdad = parseInt(edad) > 0 && parseInt(edad) <= 150;
        validar($(this), formato.test(edad) && rangoEdad);
    })
})