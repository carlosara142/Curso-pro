# a = "Hola "
# b = "Mundo"

# print (a + b) # Concatenación de cadenas

# a = "Hola "
# b = 2
# print(f"{a} {b}") # Concatenación de cadena con número usando f-string  

# ESTRUCTURA DE DATOS
# Listas
#           0        1         2          3
# frutas = ["lima", "banana", "frutilla", "naranja"]
# print("===========================\n")
# unc=int(input("Ingrese  número del 0 al 3 para seleccionar una fruta: "))
# print(frutas[unc])
# frutas.remove("banana") # Elimina un elemento de la lista
# print(frutas)
# frutas.append("kiwi") # Agrega un elemento al final de la lista
# print(frutas)
# frutas.sort() # Ordena la lista alfabéticamente
# print(frutas)   
# frutas.sort(key=len) # Ordena la lista por longitud de las palabras
# print(frutas)

# Tuplas
# #Son inmutables, no se pueden modificar después de su creación
# #        0        1        2
# dni= (12345678, "Juan", "Pérez" )
# print(dni)
# dni_uno , dni_dos , dni_tres = dni # Desempaquetado de tupla
# print(dni_uno) # Imprime el primer elemento de la tupla
# print(dni_dos) # Imprime el segundo elemento de la tupla
# print(dni_tres) # Imprime el tercer elemento de la tupla    

# Diccionarios
# Son estructuras de datos que almacenan pares clave-valor   
# diccionario = {"clave1": "valor1", "clave2": "valor2", "clave3": "valor3"}
# print(diccionario)
# print(diccionario["clave1"]) # Accede al valor asociado a "clave1"
# persona1= {
#             "nombre": "Juamn",
#             "apellido": "Pérez",
#             "edad": 30, 
#             "ciudad":"Buenos Aires"}
# print(persona1) # Imprime el diccionario completo
# print(persona1["edad"]) # Imprime el valor asociado a la clave "edad"   
# print(persona1.get("ciudad")) # Imprime el valor asociado a la clave "ciudad" usando el método get()
# persona1["profesion"] = "Ingeniero" # Agrega una nueva clave-valor al diccionario
# print(persona1) # Imprime el diccionario actualizado con la nueva clave-valor   
# print(persona1.keys()) # Imprime las claves del diccionario
# print(persona1.values()) # Imprime los valores del diccionario  
# print(persona1.items()) # Imprime los pares clave-valor del diccionario como tuplas 

# Usuarios= [
#     {
#             "nombre": "Jhuan",
#             "apellido": "Pérez",
#             "edad": 30, 
#             "ciudad":"Buenos Aires"},
#             {
#             "nombre": "María",
#             "apellido": "Gómez",
#             "edad": 25, 
#             "ciudad":"Córdoba"},
#             ]
# persona= {
#             "nombre": "Juamn",
#             "apellido": "Pérez",
#             "edad": 30, 
#             "ciudad":"Buenos Aires"}

# for i in persona:
#     print(persona[i]) # Imprime los valores del diccionario 

#Funciones

# def saludo():
#     return "¡Hola! Bienvenido a la clase de Python" # La función devuelve un mensaje de saludo  
#     print("¡Hola! Bienvenido a la clase de Python") 

# print(saludo()) # Imprime el valor devuelto por la función saludo()
# saludo() # Llamada a la función saludo() para ejecutar su código

# def saludo(nombre):
#     return f"¡Hola {nombre}! Bienvenido a la clase de Python" # La función devuelve un mensaje de saludo personalizado usando el parámetro nombre   

# print(saludo("Juan")) # Imprime el valor devuelto por la función saludo() con el argumento "Juan"
# print(saludo("María")) # Imprime el valor devuelto por  la función saludo() con el argumento "María" para ejecutar su código y obtener un saludo personalizado

def suma(a, b):
    return a + b # La función devuelve la suma de los parámetros a y b  
resultado = suma(5, 3) +2 # Llama a la función suma() con los argumentos 5 y 3, y almacena el resultado en la variable resultado   

print(resultado+4) # Imprime el valor almacenado en la variable resultado, que es la suma de 5 y 3
