#1. Calcular el factorial de un número. Luego, utilizar esa función para calcular y mostrar el factorial de todos los numeros enteros entre 1 y el numero que indique el usuario.
#Factorial de un número:
def fac(n):
    if n <= 1:
       return 1
    else: 
        return n* fac(n-1)

#Nro ingresado por usuario:
n=int(input("Ingrese un número entero: "))

#Bucle para recorrer los números entre 1 y el número ingresado por el usuario:
for i in range(1, n+1):
   print(f"{i}! = {fac(i)}")

