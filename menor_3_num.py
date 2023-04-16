# input
a = int(input("ingrese el primer número: "))
b = int(input("ingrese el segundo número: "))
c = int(input("ingrese el tercer número: "))

# processing
if a < b:
    if a < c:
        x = a  #print("El número menor es: ", a)

elif b<c:
    x = b  #print("El número menor es: ", b)

else:
    x = c  #print("El número menor es: ", c)

# output

print("El número menor es: ", x)
