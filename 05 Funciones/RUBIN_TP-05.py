
#1) Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.
mensaje="Hola mundo!" 
def hola_mundo(mensaje):
    print(mensaje) 
#principal
hola_mundo(mensaje)

#2)Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.
def saludar_usuario(nombre):
    saludo="Hola " + nombre + "!"
    return saludo

#principal
nombre=input("Ingreśa tu nombre: ")
print(saludar_usuario(nombre))

#3) Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
def informacion_personal(nombre,apellido,edad,residencia):
    informacion = (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
    print(informacion)

#principal
nombre=input("Ingresá tu nombre: ")
apellido=input("Ingresá tu apellido: ")
edad=input("Ingresá tu edad: ")
residencia=input("Ingresá tu residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

#4) Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
def calcular_perimetro_circulo(radio):
    perimetro= (2*pi*radio)
    return perimetro

def calcular_area_circulo(radio):
    area= (pi*(radio**2))
    return area

#principal 
pi=3.1416
radio = int(input("Ingrese el radio del círculo: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

perimetro = calcular_perimetro_circulo(radio)
area= calcular_area_circulo(radio)
print("El perímetro del círculo es: ",perimetro, ". El area es: ",area )

#5)Crear una función llamada segundos_a_horas(segundos) que recibauna cantidad de segundos como parámetro y devuelva la cantidad e horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas=segundos/3600
    return horas
#principal
segundos=int(input("Ingrese los segundos:"))
horas= segundos_a_horas(segundos)
print(f"{segundos} segundos es igual a {horas} horas.")

#6) Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_de_multiplicar(numero):
    for i in range(1,11):
        multiplicar=numero
        multiplicar*=i
        print(f"{numero} x {i} = {multiplicar}")
#principal
numero = int(input("Ingrese un número: "))
tabla_de_multiplicar(numero)

#7)Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
sum = 0
res = 0
mult = 0
div = 0

def operaciones_basicas(n1,n2):
    sum=n1+n2
    res=n1-n2
    div=n1/n2
    mult=n1*n2
    print(f" Suma: {sum}\n Resta: {res}\n Multiplicación: {mult}\n División: {div}")

#principaln1/n2
n1=int(input("Ingrese un número: "))
n2=int(input("Ingrese un número: "))
operaciones_basicas(n1,n2)

#8) Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso,altura):
    imc=peso/(altura**2)
    print(f"Su índice de masa corporal es: {imc:.2f}")
#principal
peso=float(input("Ingrese su peso en kg: "))
altura=float(input("Ingrese su altura en m²: "))
calcular_imc(peso,altura)

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.
def celsius_a_fahrenheit(celsius):
    fahrenheit=(celsius*9)/5+32
    return fahrenheit

#principal
celsius=float(input("Ingrese la temperatura en grados celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius) #llamo a la función y lo que devuelve lo guardo en la variable fahrenheit.
print(f"Los grados ingresados corresponden a {fahrenheit}° Fahrenheit")

#10) Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.
def calcular_promedio(a,b,c):
    sum=a+b+c
    prom= sum/3
    return prom

#principal
a=int(input("Ingrese un número: "))
b=int(input("Ingrese un número: "))
c=int(input("Ingrese un número: "))
prom = calcular_promedio(a,b,c)
print(f"El promedio de los tres números ingresados es de: {prom:.2f}")