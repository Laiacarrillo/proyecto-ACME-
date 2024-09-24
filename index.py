from grupos.grupo import registro_grupo
from modulos.modulos import registro_modulo
from user_estudiantes.estudiantes import registro_estudiante
from docentes.docentes import registro_docente
from asistencia.asistencia import registro_asistencia
from cambio_contra.cambio  import cambiar_contrasena
from interfaz.menu import menu 

while True:
    opcion = input()
    if opcion == "a":
        registro_grupo()
    elif opcion == "b":
        registro_modulo()
    elif opcion == "c":
        registro_estudiante()
    elif opcion == "d":
        registro_docente()
    elif opcion == "e":
        registro_asistencia()
    # elif opcion == "f":
    #     consultar_informacion()
    # elif opcion == "g":
    #     generar_informes()
    elif opcion == "h":
        cambiar_contrasena()
    elif opcion == "i":
        print("Salida del sistema...")
        break
    else:
        print("Opción no válida.")
        input("Presione cualquier tecla para volver al menú...")

    