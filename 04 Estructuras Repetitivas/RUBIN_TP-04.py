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
#4)Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0."""
suma=0
nro=int(input("Por favor ingrese un número entero (0 para detener): "))
while nro != 0:
    suma+=nro
    nro = int(input("Ingrese otro número (0 para detener): "))
print(suma)