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

let mensaje = mostrarProducto(productos[0], producto.precio);
console.log(mensaje);
