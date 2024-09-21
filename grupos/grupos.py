def registro_grupo():
    codigo=input("Ingrese el código del grupo: \n")
    nombre=input("Ingrese el nombre del grupo:  \n")
    grupos[codigo]=nombre
    print(f"Grupo '{nombre}' fue registrado")
