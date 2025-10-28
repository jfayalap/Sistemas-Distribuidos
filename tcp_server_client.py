## El siguiente codigo tiene como objetivo generar una comunicacion entre cliente y servidor mandando un mensaje de Hola Mundo
##donde se le pide al cliente que ingrese El IP del servidor y el host y, si coincide el servidor recibe el mensaje de Hola mundo 


import socket

IP_SERVIDOR = '127.0.0.1' #definimos el IP del servidor
PUERTO = 12000 #El valor del Host lo defini, puede ser cualquiera siempre y cuando sea superior a 10000

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((IP_SERVIDOR, PUERTO))
    servidor.listen(1)
    print(f"Servidor escuchando en {IP_SERVIDOR}:{PUERTO}...")

    conn, addr = servidor.accept()
    print(f" Conexión establecida con {addr}")

    mensaje = conn.recv(1024).decode()
    print(f" Mensaje recibido: {mensaje}") ## Este print arroja el mensaje de Hola mundo siempre 
                                            ##y cuando sea igual al puerto y IP

    conn.close()
    servidor.close()

if __name__ == '__main__':
    iniciar_servidor()

## Codigo cliente 

import socket

def iniciar_cliente():
    ip = input("Ingrese la IP del servidor : ")
    puerto = int(input("Ingrese el puerto del servidor : "))

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        cliente.connect((ip, puerto))
        mensaje = "HOLA MUNDO"
        cliente.send(mensaje.encode())
        print(" Mensaje enviado al servidor.")
    except Exception as e:
        print(f" Error al conectar con el servidor: {e}")
    finally:
        cliente.close()

if __name__ == '__main__':
    iniciar_cliente()
