import json
import os

def registro_grupo():
    grupo = {}
    codigo = input("Ingrese el código del grupo: \n")
    grupo["codigo"] = codigo
    grupo["nombre"] = input("Ingrese el nombre del grupo:  \n")
    grupo["sigla"] = input("Ingrese la sigla del grupo:  \n")

    archivo_json = os.path.join('data', 'grupo.json')

    try:
        with open(archivo_json, 'r') as f:
            grupos = json.load(f)
    except FileNotFoundError:
        grupos = {} 

    grupos[codigo] = grupo
    print(f"Grupo '{grupo['nombre']}' fue registrado")

    grupos_json = json.dumps(grupos, indent=4)

    with open(archivo_json, 'w') as f:
        f.write(grupos_json)

registro_grupo()
