#INTRODUCIMOS TEXTO A CIFRAR

texto=input ("tu texto:  ")
#CREAMOS CADENA DE CARÁCTERES

if texto==texto.upper () : #PARA MAYUSCULAS

      abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

else:

      abc="abcdefghijklmnñopqrstuvwxyz" #PARA MINUSCULAS

#DEFINIMOS VALOR DE DESPLAZAMIENTO
k=int (input ("Valor de desplazamiento: "))

#CREAMOS LA CADENA "cifrad".
cifrad=""

#REALIZAMOS CIFRADO.
for c in texto:
 if c in abc:
      cifrad += abc[(abc.index(c)+k)%(len(abc))]
 else:
     cifrad+=c

#VISUALIZAMOS TEXTO FINAL.
print("texto cifrado: ",cifrad)