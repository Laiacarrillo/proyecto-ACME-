import hashlib
import getpass
import os
import menu


contra_predefinida = "SISGESA"
archivo_contra= "contra.txt"

def hash_contra(contra):   #Encriptar la contraseña usando SHA-256
    sha256 = hashlib.sha256()
    sha256.update(contra.encode("utf-8"))
    return sha256.hexdigest()

def guardar_contra(contra): #Guarda la contraseña encriptada en un archivo
    with open(archivo_contra, "w") as f:
        f.write(hash_contra(contra))

def  cargar_contra(): #Carga la contraseña encriptada del archivo
    if os.path.exists(archivo_contra):
        with open(archivo_contra, "r") as f:
            return f.read()
    else:
        return None

def cambia_contra(): # Cambia la contraseña actual
    actual_contra = getpass.getpass("Ingrese la contraseña actual: ")
    if hash_contra(actual_contra) == cargar_contra():
        nueva_contra = getpass.getpass("Ingrese la nueva contraseña: ")
        guardar_contra(nueva_contra)
        print("Contraseña cambiada con éxito")
    else:
        print("Contraseña incorrecta")
    
def login():#Inicio de sesión
    usuario = input("Ingrese su nombre de usuario: ")
    contra = getpass.getpass("Ingrese su contraseña: ")
    if cargar_contra() is None: # Primera vez que se ejecuta el sistema
        if contra == contra_predefinida:
            guardar_contra(contra)
            print("Bienvenido al sistema")
        else:
            print("Contraseña incorrecta")
    elif hash_contra(contra) == cargar_contra():
        print("Bienvenido al sistema")
        menu()
    else:
        print("Contraseña incorrecta")


login()

