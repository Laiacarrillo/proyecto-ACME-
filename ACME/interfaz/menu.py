import json
from datetime import datetime, timedelta
import os 
from modelo.modelo import *
import getpass 
from interfaz.login import hash_contra, cargar_contra, guardar_contra



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
def registro_asistencia():
    dia = {}
    codigo_est = input('Digite el código de estudiante: ')
    if codigo_est not in estudiantes:
        print('El código del estudiante no esta registrado')
        return
    dia['codigo'] = codigo_est
    dia['codigoModulo'] = input('Digite el código del módulo: ')
    if dia['codigoModulo'] not in modulos:
        print('El codigo del modulo no existe')
        return
    hora_entrada = input('Digite la hora de ingreso (Formato 24 horas):')
    hora_entradaF = datetime.strptime(hora_entrada, '%H:%M')
    dia['horaEntrada'] = hora_entradaF
    hora_salida = input('Digite la hora de  (Formato 24 horas):')
    hora_salidaF = datetime.strptime(hora_salida, '%H:%M')
    dia['horaSalida'] = hora_salidaF
    dia['horaEntrada'] = datetime.strftime(dia['horaEntrada'], '%H:%M')
    puntualidad = dia['horaEntrada'] - modulos[dia['codigoModulo']]['horaEntrada']
    if puntualidad > timedelta(minutes=10):
        dia['puntialidad'] = 'El estudiante llegó tarde.'
    else:
        dia['puntialidad'] = 'El estudiante llegó puntual.'
    dia['horaSalida'] = datetime.strftime(dia['horaSalida'], '%H:%M')

    archivo_json = os.path.join('data', 'asistencia.json')

    try:
        with open(archivo_json, 'r') as f:
            asistencias = json.load(f)
    except FileNotFoundError:
        asistencias = {}  
    asistencias[codigo_est] = dia
    print("Se ha registrado la asistencia")
    asistencias_json = json.dumps(asistencias, indent=4)

    with open(archivo_json, 'w') as f:
        f.write(asistencias_json)



def cambia_contra(): # Cambia la contraseña actual
    actual_contra = getpass.getpass("Ingrese la contraseña actual: ")
    if hash_contra(actual_contra) == cargar_contra():
        nueva_contra = getpass.getpass("Ingrese la nueva contraseña: ")
        guardar_contra(nueva_contra)
        print("Contraseña cambiada con éxito")
    else:
        print("Contraseña incorrecta")

def menu():
    while True:
        print(" ***MENÚ*** ")
        print("a. Registro de grupos.")
        print("b. Registro de módulos.")
        print("c. Registro de estudiantes.")
        print("d. Registro de docentes.")
        print("e. Registro de asistencia.")
        print("f. Consultas de información.")
        print("g. Generación de informes.")
        print("h. Cambio de contraseña.")
        print("i. Salida del sistema.")

        opcion = input(">>>Ingrese una opción: ")
        match opcion:
            case "a":
                registro_grupo()
            case "b":
                registro_modulo()
            case "c":
                registro_estudiante()
            case "d":
                registro_docente()
            case "e":
                registro_asistencia()
            # case "f":
            #     consultar_informacion()
            # case opcion == "g":
            #     generar_informes()
            case  "h":
                cambia_contra()
            case "i":
                print("Salida del sistema...")
                break
            case _:
                print("Opción no válida.")
                input("Presione cualquier tecla para volver al menú...")