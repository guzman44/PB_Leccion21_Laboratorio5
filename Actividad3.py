################################################################
# Actividad 3. Uso de Bases de Datos No Relacionales NoSQL.
################################################################

################################################################
# Paso 1. Trabajando con Mongo DB.
################################################################
#Instalar la libreria: py -3.13 -m pip install pymongo

import pymongo

from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["mi_base"]
coleccion = db["Estudiantes"]

# Insertar documentos
coleccion.insert_many([
    { "nombre": "Juan", "edad": 20, "ciudad": "Bogotá" },
    { "nombre": "Ana", "edad": 22, "ciudad": "Medellín" },
    { "nombre": "Luis", "edad": 19, "ciudad": "Cali" }
])

# Consultar todos los documentos
print("Todos los estudiantes:")
for estudiante in coleccion.find():
    print(estudiante)

# Filtrar por ciudad
print("\nEstudiantes de Medellín:")
for estudiante in coleccion.find({"ciudad": "Medellín"}):
    print(estudiante)

# Estudiantes mayores de 20
print("\nEstudiantes mayores de 20:")
for estudiante in coleccion.find({"edad": {"$gt": 20}}):
    print(estudiante)