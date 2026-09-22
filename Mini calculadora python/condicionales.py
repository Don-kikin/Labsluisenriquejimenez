#Condicionales : Son fragmento de código que se ejecutan si es que la condición se cumple, es decir si es true, si la condición es false 
#no se ejecuta. Podemos la posibilidad de indicarle a mi programa que si una condición no se cumple se ejecute otro fragmento de código 
#Para esto tenemos palabras reservada como if(si), else(si no) y else if (si no si )que en python se usa como elif

#Condición para poder votar segun tu mayori de edad 
edad = 17

if edad >= 18:
    print("Puedes votar")
else :
    print("Eres menor de edad")

#Condición para corroborar que la contraseña coincide     
contraseña = "takisfuego18"
contraseña_verificada = "takisguego18"

if contraseña == contraseña_verificada:
    print("contraseña correcta")
else : 
    print("Contraseña incorrecta, vuelve a interntarlo")
    

#Condición con if, elif y else 
#Una tienda en línea quiere aplicar descuentos a sus clientes según el total de su compra.
#Si la compra es menor a $500, no recibe descuento.
#Si la compra es de $500 a $999, recibe un 10% de descuento.
#Si la compra es de $1,000 a $1,999, recibe un 15% de descuento.
#Si la compra es de $2,000 o más, recibe un 20% de descuento.

total_compra = 499

if total_compra >= 2000:
    print("Obtienes un 20% de descuento")
elif total_compra >= 1000:
    print("Tienes un 15% de descuento")
elif total_compra >= 500:
    print("Tienes un 10% de descuento")
else :
    print("Lo siento tu compra no tiene descuento")
    
    
#En este ejemplo tenemos un if anidado dentro de un if, tomando en cuenta que hay dos condiciones distintas a cumplir     
#Una tienda en línea quiere determinar los beneficios que recibirá un cliente según el monto de su compra y si pertenece al programa 
#de membresía.
#Si la compra es de $1,000 o más, el cliente puede obtener envío gratuito.
#Si además es miembro, recibirá un cupón del 10% para su próxima compra.
#Si no es miembro, solo recibirá el envío gratuito.
#Si la compra es menor a $1,000, no obtiene envío gratuito.
#Si es miembro, recibirá un cupón del 5% para su próxima compra.
#Si no es miembro, no recibirá ningún beneficio.
    
monto_total = 800
cliente_premium = True

if monto_total >= 1000:
    print("Felicidades, tu compra tiene envio gratis")
    if cliente_premium == True:
        print("Además, recibes un cupón del 10% para tu próxima compra.")
    else:
        print("No recibes un cupón porque no eres miembro.")

else:
    print("Tu compra no alcanza el monto para envío gratis.")

    if cliente_premium == True:
        print("Pero recibes un cupón del 5% por ser miembro.")
    else:
        print("No obtienes beneficios en esta compra.")
        
        
