from ast import JoinedStr
import socket 
import threading 

# configuracion  

usuario = "jose"
clave = "12345"
desplazamiento = 3 #para el cifrado de cesar 
    
#Cifrado de Cesar 

def cifrar(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) - base + desplazamiento) % 26 + base)
        else:
            resultado += char
    return resultado

def descifrar(texto, desplazamiento):
    return cifrar(texto, -desplazamiento)


#servidor 

def servidor ():
    s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9000))
    s.listen(1)
    print("Esperando la conexion del servidor ")

    conn, adr, = s.accept()
    print(f"Conectado con {adr}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"el paquete fue codificado {data}")
        mensaje = descifrar(data, desplazamiento)
        print(f"el paquete fue decodificado: {mensaje}")
    
    conn.close()

#cliente 

def cliente():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 9000))
    mensaje = "f{usuario}: {clave}: hola desde el nodo cliente"
    codificado = cifrar(mensaje, desplazamiento)
    print (f"Enviando el paquete codificado : {codificado}")
    s.sendall(codificado.encode())
    s.close()

# Lanzamiento
modo = input("¿Modo servidor (s) o cliente (c)? ").strip().lower()
if modo == 's':
    servidor()
elif modo == 'c':
    cliente()  
