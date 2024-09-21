def registro_modulo():
    codigo=input("Ingrese el código del módulo: \n")
    nombre=input("Ingrese el nombre del módulo:  \n")
    modulos[codigo]=nombre
    print(f"Módulo '{nombre}' fue registrado")