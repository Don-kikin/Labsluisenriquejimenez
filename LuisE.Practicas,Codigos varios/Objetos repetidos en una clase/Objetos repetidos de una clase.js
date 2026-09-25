
class Producto {
    constructor(nombre, precio, disponible) {
        this.nombre = nombre;
        this.precio = precio;
        this.disponible = disponible;
    }

    mostrarInfo() {
        console.log("El producto " + this.nombre + " cuesta $" + this.precio);
    }
}

const p1 = new Producto("Labial", 150, true);
const p2 = new Producto("Rímel", 180, false);
const p3 = new Producto("Base", 250, true);

p1.mostrarInfo();
p2.mostrarInfo();
p3.mostrarInfo();