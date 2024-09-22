import json
import os


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
            registrar_modulo()
        elif opcion == "c":
            registrar_estudiante()
        elif opcion == "d":
            registrar_docente()
        elif opcion == "e":
            registrar_asistencia()
        elif opcion == "f":
            consultar_informacion()
        elif opcion == "g":
            generar_informes()
        elif opcion == "h":
            cambiar_contrasena()
        elif opcion == "i":
            print("Salida del sistema...")
            break
        else:
            print("Opción no válida.")
            input("Presione cualquier tecla para volver al menú...")

menu()