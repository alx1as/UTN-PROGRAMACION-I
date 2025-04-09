"""#1)Imprimir en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(101):
    print(i)
#2) Solicitar al usuario un número entero y determine la cantidad de dígitos que contiene.
nro=(input("Por favor, ingrese un número entero: "))
count = 0
for i in range(len(nro)):
    count+=1
print(f"Cantidad de dígitos: ", count)
#3)Sumar todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores
n1=int(input("Por favor ingrese el primer número: "))
n2=int(input("Por favor ingrese el segundo número: "))
suma=0
if(n1<n2): #si n1 es menor a n2:
    for n1 in range(n1+1,n2):
        suma+=n1
else:
    for n2 in range(n2+1,n1): #si n2 es menor a n1
        suma+=n2
print(suma)
#4)Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
suma=0
nro=int(input("Por favor ingrese un número entero (0 para detener): "))
while nro != 0:
    suma+=nro
    nro = int(input("Ingrese otro número (0 para detener): "))
print(suma)

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
intentos=0
nro= random.randint(1,9)
nroUser = int(input("Por favor, ingrese un número del 1 al 9: "))

while nroUser !=nro:
    nroUser = int(input("Incorrecto. Por favor ingrese otro número: "))
    intentos+=1
print(f"Acertaste, felicidades! el número correcto es {nro}. Lo conseguiste en {intentos} intentos.")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
for i in range(100,0,-2):
    print(i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
tope= int(input("Ingrese un número positivo: "))
suma = 0
for i in range(0,tope+1):
    suma+=i
print(f"La suma de todos los números comprendidos entre 0 y {tope} es de: {suma}")

#8)Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).
pares=0
impares=0
negativos=0
positivos=0

for i in range(100):
    nroUser=int(input("Por favor, ingrese un número entero: "))
    if nroUser%2==0:
        pares+=1
    else:
        impares+=1
    if nroUser>0:
        positivos+=1
    else:
        negativos+=1
print(f"En total hay:\n {(pares)} números pares.\n {(impares)} números impares.\n {(positivos)} números positivos.\n y {(negativos)} números negativos.")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor)."""
suma=0
for i in range(100):
    nro=int(input("Por favor, ingrese un número entero: "))
    suma+=nro
print("El promedio de todos los números ingresados es de: " ,suma/100)

#10)  Desarrolla un programa que calcule el factorial de un número entero dado por el usuario. Ejemplo: para el número 5, el resultado debe ser 5! = 5 × 4 × 3 × 2 × 1
