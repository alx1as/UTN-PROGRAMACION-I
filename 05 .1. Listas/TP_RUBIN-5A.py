#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
for i in list(range(4,101,4)):
        print(i)
    #Acá me doy cuenta que con lista probablemente se refiera a un array asi que voy a hacerlo de nuevo:
multiplos_4 = list(range(4,101,4))
print(multiplos_4)

#2) Crear una lista con 5 elementos y mostrar el penúltimo.
elementos=["mesa", "cubo", "perro", "palta", "música"]
print(elementos[3])
  
#3) Crear lista vacía y luego agregar tres elementos e imprimirlos por pantalla.
lista= []
#No usé append porque no me permitía agregar los 3 elementos en una línea al menos que los agregue como una lista. Pero ahí devolvia una lista dentro de otra: [["hola", "como", "estas"]]
lista.extend(["hola", "como", "estas"]) #extend() itera sobre los elementos del argumento y los agrega uno por uno a la lista existente.
print(lista)

#4) Reemplazar el segundo y último valor de la lista "animales" con las palabras "loro" y "oso". Imprimir la lista resultante.
animales= ["perro", "gato", "conejo", "pez"]
animales[1]="loro"
animales[-1]="oso" #Con el index negativo comienzo a contar el índice desde la derecha.
print(animales)

#5)Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza:
numeros = [8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros)
#En este programa se crea una lista con 5 números positivos aparentemente elegidos al azar.
#Luego, a la lista se le aplica la función remove que eliminará un número seleccionado. En este caso, con la función max() se eliminará el número más grande de la lista, en este caso 22. 
#Finalmente devolverá [8,15,3,7]

#6)Crear una lista con los números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

del10_30=list(range(10,31,5))
print(del10_30[0:2])

#7)  Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera. 

autos = ["sedan", "polo", "suran", "gol"]
autos[1]=4
autos[2]="Apu"
print(autos)

#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.
dobles=[]
dobles.append(10)
dobles.append(20)
dobles.append(30)
print(dobles)

#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]
compras[0].remove("pan")#c) 
compras[1][1]="tallarines"#b)
compras[2].append("jugo")#a)
print(compras)

#10) Elaborar una lista animada llamada "lista_anidada" que contenga lo siguiente:
"""
● Posición lista_anidada[0]: 15
● Posición lista_anidada[1]: True
● Posición lista_anidada[2][0]: 25.5
● Posición lista_anidada[2][1]: 57.9
● Posición lista_anidada[2][2]: 30.6
● Posición lista_anidada[3]: False
Imprimir el resultado por pantalla.
"""
lista_anidada= [15,True,[25.5, 57.9, 30.6], False]
print(lista_anidada)
