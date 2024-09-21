def registro_estudiante():
    codigo=input("Ingrese el código: \n")
    nombre=input("Ingrese el nombre:  \n")
    sexo=input("Ingrese el sexo: \n")
    edad=int(input("Ingrese la edad \n"))
    estudiantes[codigo]=nombre
    print(f"Estudiante '{nombre}' fue registrado")