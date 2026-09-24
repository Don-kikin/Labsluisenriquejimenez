#Operadores aritméticos 

#Suma (+)
suma = 8 + 7
print(suma)

#Resta (-)
resta = 12 - 3
print(resta)

#Multiplicación (*)
multiplicacion = 15 * 6
print(multiplicacion)

#División (/) la división nos devuelve un dato float (flotante), es decir con decimal 
division = 8 / 2
print(division)

#Potenciación (exponente) (**)
exponente = 12 ** 5
print(exponente)

#División baja (//) siempre redondea hacia abajo 
division_baja = 25 // 5
print(division_baja)

#Resto a modulo (%)
resto = 74 % 9
print(resto)


#Operadores de comparación : Nos permiten comparar distintas situaciones (comparan el primer valor con el segundo) 
# y nos devuelven un true o un false 

# Es igual que ==
igualdad = 5 == 7
print(igualdad)

# Es distinto de !=
distinto_que = 5 != 5
print(distinto_que)

# Menor que <
menor = 5 < 6
print(menor)

# Menor o igual que <=
menor_igual = 7 <= 9
print(menor_igual)

# Mayor que >
mayor = 21 > 20
print(mayor)

# Mayor o igual que >=
mayor_que = 52 <= 52
print(mayor_que)

#Operadores lógicos 
#And & : Compara una condición y solo da True si la condición se cumple, de lo contrario nos devuelve un false
and_ejemplo = 5 > 3 and 10 > 8
print(and_ejemplo)  # True

and_ejemplo2 = 5 > 8 and 10 > 3
print(and_ejemplo2)  # False

#Or | : Compara una condición y solo da True si es que una de las condiciones se cumple, solo en caso de que ninguna de las condiciones 
#se cumpla arroja false 
or_ejemplo = 5 > 8 or 10 > 3
print(or_ejemplo)  # True

or_ejemplo2 = 5 > 8 or 10 > 15
print(or_ejemplo2)  # False

#Not not : Nos invierte el valor, si le damos un True nos devuelve un false y viceversa
not_ejemplo = not (5 > 3)
print(not_ejemplo)  # False

not_ejemplo2 = not (5 > 8)
print(not_ejemplo2)  # True

