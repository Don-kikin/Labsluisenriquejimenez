#Elaboracion de mini calculadora
nombre = input("Por favor, ingresa tu nombre: ")    
def saludo(nombre):
        return f"Hola {nombre}, bienvenido a la mini calculadora."
print(saludo(nombre))   

print("Por favor, selecciona que funcion deseas realizar:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Escribe la opción deseada: ")  

if opcion == '1':
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    def suma(num1, num2):
        resultado_suma = num1 + num2
        return resultado_suma
    resultado = suma(num1, num2)
    print("El resultado de la suma es:", resultado)


elif opcion == '2':
    num1 = float(input("Ingrese el primer número: "))   
    num2 = float(input("Ingrese el segundo número: "))
    def resta(num1, num2):
        resultado_resta = num1 - num2
        return resultado_resta
    resultado = resta(num1, num2)
    print("El resultado de la resta es:", resultado)

elif opcion == '3':
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    def multiplicacion(num1, num2):
        resultado_multiplicacion = num1 * num2
        return resultado_multiplicacion
    resultado = multiplicacion(num1, num2)
    print("El resultado de la multiplicación es:", resultado)

elif opcion == '4':
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    def division(num1, num2):
        if num2 != 0:
            resultado_division = num1 / num2
            return resultado_division
        else:
            return "Error: No se puede dividir entre cero."
    resultado = division(num1, num2)
    print("El resultado de la división es:", resultado)

#Bonus  
print("¿Deseas potenciar tu resultado?")
opcion_potencia = input("Escribe 's' para sí o 'n' para no: ")

if opcion_potencia == 's':
    base = float(input("Ingrese la base: "))
    exponente = float(input("Ingrese el exponente: "))
    def potencia (base, exponente):
        return base ** exponente
    resultado_potencia = potencia(base, exponente   )
    print("El resultado de la potencia es:", resultado_potencia)
else:
    print("Gracias" + nombre + " por usar la mini calculadora. ¡Hasta luego!")
