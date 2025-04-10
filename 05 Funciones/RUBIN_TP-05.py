
"""#1) Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.
mensaje="Hola mundo!" 
def hola_mundo(mensaje):
    print(mensaje) 
#principal
hola_mundo(mensaje)

#2)Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario."""
def saludar_usuario(nombre):
    saludo="Hola " + nombre + "!"
    return saludo

#principal
nombre=input("Ingreśa tu nombre: ")
print(saludar_usuario(nombre))