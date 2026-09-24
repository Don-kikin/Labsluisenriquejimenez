# Calculadora Básica en JavaScript (calculadora-js)

Este repositorio contiene una calculadora sencilla desarrollada en JavaScript como parte de un laboratorio práctico[cite: 2]. El programa solicita dos números al usuario, realiza cuatro operaciones aritméticas fundamentales y muestra los resultados a través de la consola del navegador[cite: 2].

## Características del Proyecto

El script está diseñado para poner en práctica conceptos fundamentales de programación:
* **Declaración de variables:** Uso de la palabra clave `let` para almacenar datos de entrada y resultados[cite: 2].
* **Entrada de datos:** Uso de `prompt()` para interactuar con el usuario y capturar información[cite: 2].
* **Conversión de tipos:** Implementación de la función `Number()` para transformar el texto capturado (String) en valores numéricos (Number), garantizando la correcta ejecución de las operaciones matemáticas[cite: 2].
* **Procesamiento aritmético:** Aplicación de los operadores de suma (`+`), resta (`-`), multiplicación (`*`) y división (`/`)[cite: 2].
* **Salida de resultados:** Uso de `console.log()` para mostrar la información estructurada con etiquetas claras[cite: 2].
* **Funcionalidad extendida (Reto extra):** El script incluye una rutina inicial que solicita el nombre del usuario para emitir un saludo personalizado antes de desplegar los cálculos[cite: 2].

## Entorno de Ejecución

Debido al uso de funciones nativas de la ventana del navegador (`prompt()`), este código requiere un entorno web para funcionar correctamente[cite: 2]. 

## Instrucciones de Uso

1. Abre un navegador web de tu preferencia.
2. Accede a las herramientas de desarrollador presionando la tecla `F12` en tu teclado, o haciendo clic derecho en cualquier parte blanca de la página, seleccionando "Inspeccionar" y abriendo la pestaña "Consola"[cite: 2].
3. Copia y pega el código del programa en la consola y presiona `Enter`.
4. El sistema mostrará un cuadro de diálogo con la pregunta: "¿Cómo te llamas?"[cite: 2]. Ingresa tu nombre.
5. A continuación, el programa solicitará "Escribe el primer número" y posteriormente "Escribe el segundo número"[cite: 2]. *(Nota: En esta versión básica del código, se debe evitar ingresar el cero como segundo número)*[cite: 2].
6. La consola imprimirá el saludo personalizado seguido de los resultados precisos de la suma, resta, multiplicación y división[cite: 2].

## Pruebas y Validación

El programa ha sido validado exitosamente con distintos conjuntos de datos para asegurar su estabilidad y precisión[cite: 2]. Algunas pruebas documentadas incluyen:

* **Prueba 1:** Entradas `10` y `2`. Resultados: Suma `12`, Resta `8`, Multiplicación `20`, División `5`[cite: 2].
* **Prueba 2:** Entradas `7` y `3`. Resultados: Suma `10`, Resta `4`, Multiplicación `21`, División `2.3333333333333335`[cite: 2].
* **Prueba 3 (Decimales):** Entradas `5.5` y `2`. Resultados: Suma `7.5`, Resta `3.5`, Multiplicación `11`, División `2.75`[cite: 2].