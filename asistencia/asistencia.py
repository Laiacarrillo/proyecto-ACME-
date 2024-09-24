import os
import json
from datetime import datetime, timedelta
from modulos.modulos import modulos
from user_estudiantes.estudiantes import estudiantes
modulos = {}
estudiantes = {}

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


def consultaInformacion():
    print('Consulta de Información')
    print('1. Consultar los estudiantes matriculados en un grupo.')
    print('2. Consultar los estudiantes inscritos en un módulo')
    print('3. Consultar los docentes que imparten un módulo.')
    print('4. Consultar los estudiantes a cargo de un docente en un módulo.')
registro_asistencia()