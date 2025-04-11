
"""#1) Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.
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
print(f"{segundos} segundos es igual a {horas} horas.")"""

#6) Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_de_multiplicar(numero):
    for i in range(11):
        multiplicar=numero
        multiplicar*=i
        print(f"{numero} x {i} = {multiplicar}")
#principal
numero = int(input("Ingrese un número: "))
tabla_de_multiplicar(numero)