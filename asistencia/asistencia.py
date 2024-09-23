import os
import json
from datetime import datetime

#funcion de registro asistencia
def registro_asistencia():
    dia = {}
    codigo_est = input('Digite el código de estudiante: ')
    dia['codigo'] = codigo_est
    dia['codigoModulo'] = input('Digite el código del módulo: ')
    hora_entrada = input('Digite la hora de ingreso (Formato 24 horas):')
    hora_entradaF = datetime.strptime(hora_entrada, '%H:%M')
    dia['horaEntrada'] = hora_entradaF
    hora_salida = input('Digite la hora de  (Formato 24 horas):')
    hora_salidaF = datetime.strptime(hora_salida, '%H:%M')
    dia['horaSalida'] = hora_salidaF
    dia['horaEntrada'] = datetime.strftime(dia['horaEntrada'], '%H:%M')
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

registro_asistencia()