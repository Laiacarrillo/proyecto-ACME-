def registro_docente():
    cedula=int(input("Ingrese la cédula: \n"))
    nombre=input("Ingrese el nombre:  \n")
    docentes[cedula]=nombre
    print(f"Docente '{nombre}' fue registrado")