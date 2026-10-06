
const nombre = prompt("¿Cuál es tu nombre?");



switch (nombre) {
    case "Argelia":
        alert(`Hola ${nombre}, Estoy aquí por mejores oportunidades laborales y de crecimiento profesional. Espero del proyecto adquirir mejores habilidades técnicas. `);
        break;
    case "Kevin":
        alert(`Hola ${nombre}, Estoy aquí para aprender programación y con esa habilidad poder hacer reales mis ideas`);

        break;
    case "Luis":
        alert(`Hola ${nombre}, Aprender programacion, distintos tipos de lenguaje, javascript, python, html, lograr pivotar mi carrera hacia el desarrollo web`);
        break;
    case "Mariana":
        alert(`Hola ${nombre}, Estoy aquí para fortalecer mi conocimiento. Espero conseguir un empleo que permita crecer y desarrollar mis habilidades de programador.`);
        break;
    case "Alejandra":
        alert(`Hola ${nombre}, está aquí porque quiere aprender programación y espero que nuestro proyecto sea funcional e innovador`);
        break;
    case "Erick":
        alert(`Hola ${nombre}, Estoy aquí para estar mejor capacitado y poder entrar a un trabajo como programador y dedicarme a eso`);      
        break;
    case "Alan":
        alert(`Hola ${nombre}, Yo espero aprender mucho y estoy aqui para conseguir un trabajo Home office, y espero que nuestro proyecto sea un proyecto revolucionario donde aprendamos mucho y que nos permita desarrollarnos plenamente`);
        break;
    case "Eduardo":
        alert(`Hola ${nombre}, Estoy aqui para aprender a programar y poder conseguir un trabajo en el area de desarrollo web, lo que espero de mi ecomerce es crear un proyecto que me ayude a mejorar mis habilidades y conocimientos en el area de desarrollo web`);
        break;


    default:
        alert(`Nombre no encontrado, por favor ingresa un nombre válido.`);
        break;
}