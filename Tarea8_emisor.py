import cv2
import socket
import struct

IP_RECEPTOR = '127.0.0.1'
PUERTO = 9999

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((IP_RECEPTOR, PUERTO))

camara = cv2.VideoCapture(0)

while True:
    ret, frame = camara.read()
    if not ret:
        break

    _, buffer = cv2.imencode('.jpg', frame)
    data = buffer.tobytes()
    tamaño = struct.pack("Q", len(data))
    cliente.sendall(tamaño + data)

camara.release()
cliente.close()

