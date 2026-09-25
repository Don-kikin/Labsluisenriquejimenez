const arr = [
    [0,1,2,3,4,5,6,7,8,9],
    [10,11,12,13,14,15,16,17,18,19],
    [20,21,22,23,24,25,26,27,28,29]
  ]
  
  // Type your code below this line!
// ¿Puede agregar un solo número a una fila existente?
arr[0].push(10); 

// ¿Puede agregar una fila completamente nueva de números?
arr.push([30, 31, 32, 33, 34, 35]);

// ¿Puede eliminar un solo número de una sola fila?
arr[1].splice(1,1); 

// ¿Puede invertir una de las filas sin afectar a las demás?
arr[2].reverse();

// Imprime la matriz final fila por fila
arr.forEach(element => console.log(element));
  
  // Type your code above this line!