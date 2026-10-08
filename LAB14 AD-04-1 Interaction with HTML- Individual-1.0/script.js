// Tarea 2: Imprimir en consola al hacer clic en "Burger Town!"
const burgerTownBtn = document.getElementById("burger-town-trigger");

if (burgerTownBtn) {
  burgerTownBtn.addEventListener("click", function () {
    console.log("¡Alguien ha hecho clic en BURGER TOWN!");
  });
}

// Tarea 4: Cambiar el color del encabezado a rojo al hacer clic en "RICE!!"
const riceWord = document.getElementById("rice-trigger");
const burgerTitle = document.getElementById("burger-pic-title");

if (riceWord && burgerTitle) {
  riceWord.addEventListener("click", function () {
    burgerTitle.style.color = "red";
  });
}