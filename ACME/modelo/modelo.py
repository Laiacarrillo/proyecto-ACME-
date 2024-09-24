import json
import os

def registro_modulo():
    modulo = {}
    codigo = input("Ingrese el código del módulo: \n")
    modulo["codigo"] = codigo
    modulo["nombre"] = input("Ingrese el nombre del módulo:  \n")
    modulo["horaEntrada"] = input("Ingrese la hora de entrada:  \n")
    modulo["horaSalida"] = input("Ingrese la hora de salida:  \n")

    archivo_json = os.path.join('data', 'modulo.json')

    try:
        with open(archivo_json, 'r') as f:
            modulos = json.load(f)
    except FileNotFoundError:
        modulos = {}  

   
    modulos[codigo] = modulo
    print(f"Módulo '{modulo['nombre']}' fue registrado")

    modulos_json = json.dumps(modulos, indent=4)


    with open(archivo_json, 'w') as f:
        f.write(modulos_json)
registro_modulo()
