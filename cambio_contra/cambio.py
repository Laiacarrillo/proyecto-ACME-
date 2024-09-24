import getpass
from interfaz.login import hash_contra, cargar_contra, guardar_contra

def cambia_contra(): # Cambia la contraseña actual
    actual_contra = getpass.getpass("Ingrese la contraseña actual: ")
    if hash_contra(actual_contra) == cargar_contra():
        nueva_contra = getpass.getpass("Ingrese la nueva contraseña: ")
        guardar_contra(nueva_contra)
        print("Contraseña cambiada con éxito")
    else:
        print("Contraseña incorrecta")

cambia_contra()