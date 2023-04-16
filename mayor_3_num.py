# input
a = int(input("ingrese el primer número: "))
b = int(input("ingrese el segundo número: "))
c = int(input("ingrese el tercer número: "))

# processing
if a > b:
    if a > c:
        x = a  #print("El número mayor es: ", a)

elif b>c:
    x = b  #print("El número mayor es: ", b)

else:
    x = c  #print("El número mayor es: ", c)

# output

print("El número mayor es: ", x)
