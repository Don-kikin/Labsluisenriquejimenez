#Test 1
def addmultiplenumbers(numbers_list):
    return sum(numbers_list)

#Test 2, 3, 4
def multiplymultiplenumbers(numbers_list):
    resultado = 1
    for num in numbers_list:
        resultado *= num
    return resultado

#Test 5, 6
def isiteven(num):
    # Verificamos que sea entero y que su residuo al dividir entre 2 sea 0
    return num == int(num) and num % 2 == 0

#Test 7, 8
def isitaninteger(num):
    # Un número es entero si es exactamente igual a su versión sin decimales
    return num == int(num)

#test 9 
def main():
    print("Hello learners! La calculadora está lista.")
    
#Test 10
if __name__ == "__main__":
    main()