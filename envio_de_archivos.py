##codigo receptor 

import socket

puerto_local = 9000
tamaño_bloque = 2048

def recibir_archivo():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', puerto_local))
    s.listen(1)
    print(" Esperando archivo...")

    conn, addr = s.accept()
    print(f"Conectado con {addr}")

    # Recibir metadatos
    meta = conn.recv(1024).decode()
    if '|' not in meta:
        print(f" Error: metadatos mal formateados: {meta}")
        conn.close()
        return

    partes = meta.split('|')
    if len(partes) != 2:
        print(f" Error: se esperaban 2 partes, se recibieron {len(partes)}: {meta}")
        conn.close()
        return

    nombre, tamaño = partes
    tamaño = int(tamaño)
    conn.send(b'OK')  

    recibido = 0
    with open(f"recibido_{nombre}", 'wb') as f:
        while recibido < tamaño:
            bloque = conn.recv(tamaño_bloque)
            if not bloque:
                break
            f.write(bloque)
            recibido += len(bloque)

    print(f"Archivo recibido: recibido_{nombre}")
    conn.close()

if __name__ == '__main__':
    recibir_archivo()

##codigo emisor 

import socket
import os

ip_receptor = '127.0.0.1'
receptor = 9000
tamaño_bloque = 1024


def enviar_archivo(ruta):
    if not os.path.exists(ruta):
        print(f" Archivo no encontrado: {ruta}")
        return

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_receptor, receptor))

    nombre = os.path.basename(ruta)
    tamaño = os.path.getsize(ruta)

    # Enviar metadatos: nombre y tamaño
    s.send(f"{nombre}|{tamaño}".encode())

    # Esperar confirmación
    confirmacion = s.recv(1024)
    if confirmacion != b'OK':
        print(" Error: no se recibió confirmación del receptor.")
        s.close()
        return

    with open(ruta, 'rb') as f:
        while True:
            bloque = f.read(tamaño_bloque)
            if not bloque:
                break
            s.send(bloque)

    print(" Archivo enviado correctamente.")
    s.close()

if __name__ == '__main__':
    enviar_archivo('/Users/jayala2/Documents/maestria/sistemas-distribuidos/prueba.txt')  

