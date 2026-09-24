// Reto integrador
// Combina array, objeto y funcion en un mismo ejercicio
let productos = [
    "labial", "rimel",
    "base"
];

let producto = {
    nombre: "labial",
    precio: 150,
    disponible: true
};

function mostrarProducto(nombre, precio){
     return nombre + " cuesta $" + precio;
};

let mensaje = mostrarProducto("El producto es: " + productos[0], producto.precio);
console.log("Buen dia, bienvenido a productosbelleza.com")
console.log ("Que producto deseas: " 
    + productos)
console.log(mensaje);
