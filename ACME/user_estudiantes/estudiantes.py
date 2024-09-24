import json
import os

def registro_estudiante():
    estudiante = {}
    codigo = input("Ingrese el código: \n")
    estudiante["nombre"] = input("Ingrese el nombre:  \n")
    estudiante["sexo"] = input("Ingrese el sexo: \n")
    estudiante["edad"] = int(input("Ingrese la edad: \n"))
    estudiantes[codigo] = estudiante
    print(f"Estudiante '{estudiante['nombre']}' fue registrado")

archivo_json = os.path.join('data', 'estudiante.json')

try:
    with open(archivo_json, 'r') as f:
        estudiantes = json.load(f)
except FileNotFoundError:
    estudiantes = {}

registro_estudiante()

estudiantes_json = json.dumps(estudiantes, indent=4)

with open(archivo_json, 'w') as f:
    f.write(estudiantes_json)
