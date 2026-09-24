#Elaborar un programa que permita poner dos numeros , agregarlos y unirlos, luego imprimir el resultado.
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
resultado = num1 + num2
print("El resultado de la suma es:", resultado)

# Extra time
while True:

        print("Extra time - Elige una opción:")
        print("1. Restar, Multiplicar, Dividir o Módulo")
        print("2. Sumar 3 números")
        print("3. Operación mixta")

        opcion = input("Escribe la opción deseada: ")

        if opcion == '1':
                    n1 = float(input("Primer número: "))
                    n2 = float(input("Segundo número: "))
                    print("Elige la operación que deseas realizar:")
                    print("Resta (-)")
                    print("Multiplicación (*)") 
                    print("División (/)")
                    print("Módulo (%)")

                    op = input("Elige la operación (-, *, /, %): ")

                    if op == '-': 
                        print("Resultado:", n1 - n2)
                    elif op == '*': 
                        print("Resultado:", n1 * n2)
                    elif op == '/': 
                        print("Resultado:", n1 / n2)
                    elif op == '%': 
                        print("Resultado:", n1 % n2)
                    else:
                        print("Operación no reconocida.")   

                        print("Hasta luego.")
                    break 

        elif opcion == '2': 
                    n1 = float(input("Número 1: "))
                    n2 = float(input("Número 2: "))
                    n3 = float(input("Número 3: "))
                    print("Resultado:", n1 + n2 + n3)
                    print("Hasta luego.")
                    break
                
        elif opcion == '3':
                    expresion = input("Escribe tu operación matemática (ej. 4 * 5 + 1 / 3): ")
                    print("Resultado:", eval(expresion))
                    print("Hasta luego.")
                    break