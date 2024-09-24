import json
import os

def registro_docente():
    docente = {}
    cedula = int(input("Ingrese la cédula: \n"))
    docente["cedula"] = cedula
    docente["nombre"] = input("Ingrese el nombre:  \n")

    archivo_json = os.path.join('data', 'docente.json')

    try:
        with open(archivo_json, 'r') as f:
            docentes = json.load(f)
    except FileNotFoundError:
        docentes = {}  

    docentes[cedula] = docente
    print(f"Docente '{docente['nombre']}' fue registrado")

    docentes_json = json.dumps(docentes, indent=4)

    with open(archivo_json, 'w') as f:
        f.write(docentes_json)

registro_docente()
