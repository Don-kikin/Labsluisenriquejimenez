// =========================================
// TAREA 3 - JAVASCRIPT
// =========================================


// Cambiar el primer "Hola Mundo" a "Adiós"

let primerEncabezado = document.getElementById("red");

primerEncabezado.textContent = "Adiós";


// Cambiar un encabezado a naranja

let encabezadoNaranja = document.querySelector(".blue");

encabezadoNaranja.style.color = "orange";


// Cambiar el color del encabezado al hacer clic

let encabezadoClic = document.getElementById("encabezado-clic");

encabezadoClic.addEventListener("click", function () {

    encabezadoClic.style.color = "brown";

});