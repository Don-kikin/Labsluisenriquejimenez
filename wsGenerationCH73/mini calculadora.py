#Elaboracion de mini calculadora
print("Bienvenido a la mini calculadora")
print("Por favor, selecciona que funcion deseas realizar:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Escribe la opción deseada: ")  

while True:

        if opcion == '1':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = num1 + num2
            print("El resultado de la suma es:", resultado)
            break
        elif opcion == '2':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = num1 - num2
            print("El resultado de la resta es:", resultado)
            break
        elif opcion == '3':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = num1 * num2
            print("El resultado de la multiplicación es:", resultado)
            break
        elif opcion == '4':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            if num2 != 0:
                resultado = num1 / num2
                print("El resultado de la división es:", resultado)
            else:
                print("Error: No se puede dividir entre cero.")
            break
    
        

