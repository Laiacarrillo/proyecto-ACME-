import json
import os

def registro_modulo():
    modulo = {}
    codigo = input("Ingrese el código del módulo: \n")
    modulo["codigo"] = codigo
    modulo["nombre"] = input("Ingrese el nombre del módulo:  \n")

    # Ruta completa del archivo JSON en la carpeta 'data'
    archivo_json = os.path.join('data', 'modulo.json')

    # Leer el archivo JSON y deserializarlo a un diccionario
    try:
        with open(archivo_json, 'r') as f:
            modulos = json.load(f)
    except FileNotFoundError:
        modulos = {}  # Inicializa 'modulos' como un diccionario vacío si no existe el archivo

    # Agregar el nuevo módulo
    modulos[codigo] = modulo
    print(f"Módulo '{modulo['nombre']}' fue registrado")

    # Serializar el diccionario modulos a un string JSON
    modulos_json = json.dumps(modulos, indent=4)

    # Escribir el string JSON en el archivo dentro de la carpeta 'data'
    with open(archivo_json, 'w') as f:
        f.write(modulos_json)

# Llamada a la función para registrar el módulo
registro_modulo()
