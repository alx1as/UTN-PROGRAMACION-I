"""#1. Calcular el factorial de un número. Luego, utilizar esa función para calcular y mostrar el factorial de todos los numeros enteros entre 1 y el numero que indique el usuario.
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
   print(f"{i}! = {fac(i)}") #Llamo a la función recursiva con cada i hasta el número elegido."""

#2. Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.
#fibonacci: sucesión numérica donde cada termino es la suma de los dos anteriores. 

posicion=int(input("Especifique hasta la posición que desea ver de la serie Fibonacci: "))
#0 1 1 2 3 5 8 13 -> el valor de una posicion lo obtengo haciendo la suma del valor en n-1 y n-2
def fib(posicion):
    if posicion==0: #caso base: 0 y 1
        return 0
    elif posicion==1:
        return 1
    else:
        return fib(posicion-1) + fib(posicion-2) #suma del valor en n-1 y n-2. 
print(f"El número en la posición {posicion} de la serie Fibonacci es: {fib(posicion)}") #valor de la serie en la posición indicada
for i in range(1, posicion +1):
    print(fib(posicion-i)) #imprime desde la posición restando 1 el índice hasta el corte base de la recursión.