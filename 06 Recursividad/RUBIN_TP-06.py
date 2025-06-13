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
   print(f"{i}! = {fac(i)}") #Llamo a la función recursiva con cada i hasta el número elegido.

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
print(f"El valor de la serie Fibonacci en la posición {posicion} es: {fib(posicion)}") #valor de la serie en la posición indicada
for i in range(1, posicion +1):
    print(fib(posicion-i)) #imprime desde la posición restando 1 el índice hasta el corte base de la recursión.

#3 Crear una función recursiva  que calcule la potencia de un número base elevado a un exponente, utilizando la formula. Prueba esta función en un algoritmo general.

def potencia(base,exponente):
    if exponente==0: return 1 
#Segun la formula si quiero calcular un numero n(base) elevado a la potencia m(exponente) podria hacerlo multipliciando n por si mismo m-1 veces.
    else: return base*potencia(base, exponente-1)

def gral():
    base=int(input("Escriba la base:"))
    exponente=int(input("Escriba el exponente: "))
    resultado=potencia(base,exponente)
    print(f"La potencia de {base} elevado a {exponente} es {resultado}")
gral()

#4
Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.
Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este
procedimiento:
Dividir el número por 2.
Guardar el resto (0 o 1).
Repetir el proceso con el cociente hasta que llegue a 0.
Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario."""
def binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return binario(n // 2) + str(n % 2)
print(binario(13))

#es palindromo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

#suma de digitos
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

#8a 
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)
#8b
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    if numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    return contar_digito(numero // 10, digito)


