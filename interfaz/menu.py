from grupo.grupo import registro_grupo
from modulos.modulos import registro_modulo
from user_estudiantes.estudiantes import registro_estudiante
from docentes.docentes import registro_docente
from asistencia.asistencia import registro_asistencia


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
        # elif opcion == "h":
        #     cambiar_contrasena()
        # elif opcion == "i":
        #     print("Salida del sistema...")
        #     break
        # else:
        #     print("Opción no válida.")
        #     input("Presione cualquier tecla para volver al menú...")

menu()