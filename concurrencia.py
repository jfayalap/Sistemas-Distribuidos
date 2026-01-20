import cv2
import socket
import struct
import numpy as np

PUERTO = 9999

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('0.0.0.0', PUERTO))
servidor.listen(1)
print("🎥 Esperando conexión...")

conn, addr = servidor.accept()
print(f"🔗 Conectado con {addr}")

data = b''
payload_size = struct.calcsize("Q")

while True:
    while len(data) < payload_size:
        paquete = conn.recv(4096)
        if not paquete:
            break
        data += paquete

    tamaño = struct.unpack("Q", data[:payload_size])[0]
    data = data[payload_size:]

    while len(data) < tamaño:
        data += conn.recv(4096)

    frame_data = data[:tamaño]
    data = data[tamaño:]

    frame = cv2.imdecode(np.frombuffer(frame_data, np.uint8), cv2.IMREAD_COLOR)
    cv2.imshow("Video recibido", frame)

    if cv2.waitKey(1) == 27:
        break

conn.close()
cv2.destroyAllWindows()
