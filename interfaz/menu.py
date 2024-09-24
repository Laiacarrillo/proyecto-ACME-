from grupos.grupo import registro_grupo
from modulos.modulos import registro_modulo
from user_estudiantes.estudiantes import registro_estudiante
from docentes.docentes import registro_docente
from asistencia.asistencia import registro_asistencia
from cambio_contra.cambio  import cambiar_contrasena


def menu():
    while True:
        opc=menu()
        match opc: 
            case "a":
                registro_grupo()
            case  "b":
                registro_modulo()
            case  "c":
                registro_estudiante()
            case  "d":
                registro_docente()
            case  "e":
                registro_asistencia()
                # case opcion == "f":
                #     consultar_informacion()
                # case opcion == "g":
                #     generar_informes()
            case "h":
                cambiar_contrasena()
            case  "i":
                print("Salida del sistema...")
            case _:
                print("Opción no válida.")
                input("Presione cualquier tecla para volver al menú...")


menu()