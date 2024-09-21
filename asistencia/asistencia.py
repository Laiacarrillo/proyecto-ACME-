#diccionarios 
grupos={}
modulos={}
estudiantes={}
docentes={}
asistencia={}

#funcion de registro de grupo
def registro_grupo():
    grupo = {}
    codigo = input("Ingrese el código del grupo: \n")
    grupo["codigo"]= codigo
    grupo["nombre"]=input("Ingrese el nombre del grupo:  \n")
    grupos[codigo] = grupo
    print(f"Grupo {grupo["nombre"]} fue registrado")

#funcion de registro de modulos
def registro_modulo():
    modulo = {}
    codigo = input("Ingrese el código del módulo: \n")
    modulo["codigo"] = codigo
    modulo["nombre"]=input("Ingrese el nombre del módulo:  \n")
    modulos[codigo]=modulo
    print(f"Módulo '{modulo["nombre"]}' fue registrado")

#funcion de registro estudiantes
def registro_estudiante():
    estudiante={}
    codigo=input("Ingrese el código: \n")
    estudiante["nombre"]=input("Ingrese el nombre:  \n")
    estudiante["sexo"]=input("Ingrese el sexo: \n")
    estudiante["edad"]=int(input("Ingrese la edad \n"))
    estudiantes[codigo]=estudiante
    print(f"Estudiante '{estudiante["nombre"]}' fue registrado")

#funcion de registro docentes
def registro_docente():
    docente={}
    cedula=int(input("Ingrese la cédula: \n"))
    docente["cedula"]=cedula
    docente=input("Ingrese el nombre:  \n")
    docentes[cedula]=docente
    print(f"Docente '{docente["nombre"]}' fue registrado")

#funcion de registro asistencia
def registro_asistencia():
    codigo=input("Ingrese el código del estudiante: \n")
    codigo_modulo=input("Ingrese el códio del módulo: \n")
    sexo=input("Ingrese el sexo: \n")
    edad=int(input("Ingrese la edad \n"))
    estudiantes[codigo]=
    print(f"Estudiante '{estudiantes}' fue registrado")
    

