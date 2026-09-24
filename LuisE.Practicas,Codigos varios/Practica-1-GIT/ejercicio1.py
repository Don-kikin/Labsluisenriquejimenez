#Python es un lenguaje de alto nivel, orientado a objetos, lenguaje interpretado
#Variables : Son espacios de memoria en los que voy a almacenar distintos tipos de datos
#Cuatro tipos de datos simples

#String : Cadena de texto, se escribe con "",'',"""""",'''''
#Las comillas simples y dobles se utilizan en textos de una sola linea
#Las comillas triples se utilizan en textos multiples

from pickle import FALSE


nombre ="Luis Enrique "
ch = "CH73" 

#Numero enteros
34

#Numeros flotantes (Punto decimal)
34.4

#Booleanos (Verdadero o Falso): Se dividen en TRUE o FALSE (Se escribe con MAYUSCULAS)

True    
False  
##########################
############
#######################
######
saludo = "Hola "+ nombre + "Bienvenida " +ch
print(saludo)

#Ejercicio Input/ almaceno datos/output
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
ch = input("Ingrese su grupo: ")
dato_desconocido = input("Ingrese un dato secreto que solo usted conocia: ")

dato_random = input("Ingrese un dato curioso: ")

print("Hola " + nombre + " tu edad es " + edad + " y tu cohorte es " + ch + " el dato secreto es " + dato_desconocido + " y el dato curioso es " + dato_random)
print (nombre + "Que bonito nombre")
print (edad + "Que joven eres")
print (ch + "Estas en la mejor cohorte")
print (dato_desconocido + "Que dato tan secreto")
print (dato_random + "Que dato tan locooo"+ "Fue un gusto conocerte " + nombre)
