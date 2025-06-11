################################################################
# Actividad 1. Uso de Python básico.
################################################################

################################################################
# Paso 1: Sintaxis Básica y Operaciones Simples
################################################################
print("¡Hola! Este es mi primer programa en Python.")

entero = 20
decimal = 5.5
texto = "Python es genial"

print("Suma:", entero + int(decimal))
print("Concatenación:", texto + " y fácil de aprender")

################################################################
# Paso 2: Condicionales y Bucles
################################################################
numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print("Es par")
else:
    print("Es impar")

print("Cuadrados de números:")
for i in [1, 2, 3, 4, 5]:
    print(i, "al cuadrado es", i ** 2)

entrada = ""
while entrada != "salir":
    entrada = input("Escribe 'salir' para terminar: ")

################################################################
# Paso 3: Listas y Diccionarios
################################################################
nombres = ["Marco", "Michelle", "Rafael"]
for nombre in nombres:
    print("Estudiante:", nombre)

contacto = {"nombre": "Marco", "correo": "marco.guzman.ttc.833@unilibre.edu.co"}
for clave, valor in contacto.items():
    print(clave, ":", valor)



################################################################
# Paso 4: Script de resolución de problemas simples
################################################################
def calculadora():
    a = float(input("Número 1: "))
    b = float(input("Número 2: "))
    operacion = input("Operación (+, -, *, /): ")
    if operacion == "+":
        print("Resultado:", a + b)
    elif operacion == "-":
        print("Resultado:", a - b)
    elif operacion == "*":
        print("Resultado:", a * b)
    elif operacion == "/":
        print("Resultado:", a / b)
    else:
        print("Operación no válida")

calculadora()

import random
oculto = random.randint(1, 100)
adivina = -1
while adivina != oculto:
    adivina = int(input("Adivina el número (1-100): "))
    if adivina < oculto:
        print("Mayor")
    elif adivina > oculto:
        print("Menor")
print("¡Correcto!")