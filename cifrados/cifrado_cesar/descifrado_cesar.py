#Codigo de descfrado cesar

texto=input ("Texto cifrado a descifrar:  ")

# Creacion de las cadenas de texto
if texto==texto.upper () : #Para mayusculas

      abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

else:

      abc="abcdefghijklmnñopqrstuvwxyz" #Para minusculas

#DEFINIMOS VALOR DE DESPLAZAMIENTO
k=int (input ("Valor de desplazamiento: "))

#CREAMOS LA CADENA "cifrad".
descifrado=""

#REALIZAMOS CIFRADO.
for c in texto:
 if c in abc:
      descifrado += abc[(abc.index(c)-k)%(len(abc))]
 else:
     descifrado+=c

#VISUALIZAMOS TEXTO FINAL.
print("cifrado descifrado: ",descifrado)