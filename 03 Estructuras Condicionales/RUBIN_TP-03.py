"""# 1) Solicitar la edad del usuario. Si el usuario es mayor de 18 años, mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad = int(input("Por favor, ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")
else:
    pass

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”

nota = int(input("Ingrese su nota: "))
if nota>= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

nro = int(input("Por favor, ingrese un número par: "))
if nro % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par: ")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: Niño/a: menor de 12 años.  Adolescente: mayor o igual que 12 años y menor que 18 años. Adulto/a joven: mayor o igual que 18 años y menor que 30 años. Adulto/a: mayor o igual que 30 años. 
 
edad=int(input("Por favor ingrese su edad: "))
if edad < 12:
    print("Eres un niño")
elif edad>=12 and edad<18:
    print("Eres un adolescente")
elif edad>=18 and edad<30:
    print("Eres un adulto jóven")
elif edad>=30:
    print("Eres un adulto")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

contraseña = input("Por favor, ingrese una contraseña de 8 a 14 caracteres: ")
if len(contraseña)>7 and len(contraseña)<15: #Si la longitud de la contraseña es mayor a 7 y menor a 15
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor ingrese una contraseña de entre 8 y 14 caracteres: ")

# 6)Escribir un programa que tome los numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 

import random
from statistics import mode, median, mean
numeros_aleatorios = [random.randint(1,100) for i in range(50)] #Lista de 50 números random

media = mean(numeros_aleatorios) #es el promedio de la lista de números
mediana = median(numeros_aleatorios) #número central o promedio de 2 números centrales.
moda = mode(numeros_aleatorios) #es el número que más se repite de la lista.

if moda<mediana<media:
    print("Sesgo positivo o a la derecha")
elif media<mediana and mediana<moda:
    print("Sesgo negativo o a la izquierda")
elif media==mediana and mediana==moda:
    print("Sin sesgo")

#imprimir resultados en pantalla
print(f"Números aleatorios: {numeros_aleatorios}")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

palabra = input("Escribe una palabra o frase: ")
ultima_letra= palabra[-1] #indexación negativa para tomar última letra.
if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u":
    print(f"{palabra}!")
else:
    print(f"{palabra}")

#8) Solicitar nombre y números 1 (mayus), 2(min) o 3 (title) y preguntar.
nombre=input("Por favor escriba su nombre: ")
tipo=int(input("Por favor ingrese el número deseado. 1: Si quiere su nombre en mayúsculas. 2: Si lo quiere en minúsculas. 3: Si lo quiere con la primera letra en mayúscula: "))
if tipo==1:
    print(nombre.upper())
elif tipo==2:
    print(nombre.lower())
elif tipo==3:
    print(nombre.title())

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla

magnitud = int(input("Por favor ingrese la magnitud del terremoto: "))
if magnitud<3:
    print("Muy leve")
elif magnitud>=3 and magnitud<4:
    print("Leve. Ligeramente perceptible")
elif magnitud>=4 and magnitud<5:
    print("Moderado. Sentido por algunas personas, pero generalmente no causa daño")
elif magnitud>=5 and magnitud<6:
    print("Fuerte. Puede causar daños en estructuras débiles.")
elif magnitud>=6 and magnitud<7:
    print("Muy fuerte. Puede causar daños significativos.")
elif magnitud>=7:
    print("Extremo. Puede causar grandes daños a gran escala.")

#10)Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano."""
hemisferio = input("Ingrese en cuál hemisferio se encuentra (N/S): ")
mes = int(input("Ingrese el número del mes: "))
dia = int(input("Ingrese qué día es: "))

if hemisferio == "n" or hemisferio == "N": #hemisferio norte
    if (mes == 12 and dia >= 21) or (mes == 1 or mes == 2) or (mes == 3 and dia <= 20):
        estacion = "invierno"
    elif (mes == 6 and dia >= 21) or (mes == 7 or mes == 8) or (mes == 9 and dia <= 20):
        estacion = "verano"
    elif (mes == 9 and dia >= 21) or (mes == 10 or mes == 11) or (mes == 12 and dia <= 20):
        estacion = "otoño"
    elif (mes == 3 and dia >= 21) or (mes == 4 or mes == 5) or (mes == 6 and dia <= 20):
        estacion = "primavera"
    print(f"En el hemisferio norte es {estacion}.")

elif hemisferio == "s" or hemisferio == "S": #hemisferio sur
    if (mes == 12 and dia>=21) or (mes==1 or mes == 2) or (mes==3 and dia<=20):
        estacion = "verano"
    elif (mes == 6 and dia>=21) or (mes==7 or mes == 8) or (mes==9 and dia<=20):
        estacion = "invierno"
    elif (mes == 9 and dia>=21) or (mes==10 or mes == 11) or (mes==12 and dia<=20):
        estacion = "primavera"
    elif (mes == 3 and dia>=21) or (mes==4 or mes == 5) or (mes==6 and dia<=20):
        estacion = "otoño"
    print(f"En el hemisferio sur es {estacion}.")

else:
    print("Hemisferio no válido")



