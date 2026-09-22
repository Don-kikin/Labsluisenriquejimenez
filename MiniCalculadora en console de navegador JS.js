function sumar (a, b){
    return (a + b)
}
function restar (a, b){
    return (a - b)
}
function multiplicar (a, b){
    return (a * b)
}
function dividir (a, b){
    return (a / b)
}
let nombre = prompt ("Cual es tu nombre?")
console.log("Hola, " + nombre)

let numero=Number(prompt("Escribe el numero")); 
let numero2=Number(prompt("numero2"));
console.log("Suma: " + sumar(numero,numero2))
console.log("Resta: " + restar(numero,numero2))
console.log("Multiplicar: " + multiplicar(numero,numero2))
console.log("Division: " + dividir(numero,numero2))