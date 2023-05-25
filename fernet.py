from cryptography.fernet import Fernet

def generar_clave():
    # Genera una clave aleatoria para el cifrado
    clave = Fernet.generate_key()
    with open('clave.key', 'wb') as archivo_clave:
        archivo_clave.write(clave)

def cargar_clave():
    # Carga la clave desde un archivo
    with open('clave.key', 'rb') as archivo_clave:
        clave = archivo_clave.read()
    return clave

def cifrar_mensaje(mensaje, clave):
    # Cifra el mensaje utilizando la clave proporcionada
    f = Fernet(clave)
    mensaje_cifrado = f.encrypt(mensaje.encode())
    return mensaje_cifrado

def descifrar_mensaje(mensaje_cifrado, clave):
    # Descifra el mensaje utilizando la clave proporcionada
    f = Fernet(clave)
    mensaje_descifrado = f.decrypt(mensaje_cifrado)
    return mensaje_descifrado.decode()



