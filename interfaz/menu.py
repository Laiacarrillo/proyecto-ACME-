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

    input(">>>Ingrese una opción? ", end="")

       
    if opcion == "a":
        registrar_grupo()
    elif opcion == "b":
        registrar_modulo()
    elif opcion == "c":
        registrar_estudiante()
    elif opcion == "d":
        registrar_docente()
    elif opcion == "e":
        registrar_asistencia()
    elif opcion == "h": 
        registrar_contrasena()
    elif opcion == "i":
        print("Salida del sistema...") 
        
    else:
        print("Opción no válida. ") 
        input("Presione cualquier tecla para volver al menú...")
        

          