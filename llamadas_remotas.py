import socket
import threading
import tkinter as tk
import json

# Configuración de nodos
nodos = [
    ('127.0.0.1', 10000),
    ('127.0.0.1', 11000)
]

nodo_inicial = 1 # hay que cambiar el nodo una vez en la segunda terminal para que se genere el table del segundo jugador 
IP, PUERTO_LOCAL = nodos[nodo_inicial]
IP_REMOTO, PUERTO_REMOTO = nodos[1 - nodo_inicial]
JUGADOR = nodo_inicial + 1  


def aplicar_movimiento(gui, datos):
    gui.actualizar_casilla(datos['casilla'], datos['valor'])

funciones = {
    'movimiento': aplicar_movimiento
}

# creacion de la interfaz grafica 

class JuegoGato:
    def __init__(self, enviar_callback):
        self.root = tk.Tk()
        self.root.title(f'Gato P2P - Jugador {JUGADOR}')
        self.enviar_callback = enviar_callback
        self.turno = 1  # inicio del jugador 1
        self.tablero = [None] * 9
        self.botones = []

        for i in range(9):
            b = tk.Button(self.root, text='', font=('Arial', 28), width=5, height=2,
                          command=lambda i=i: self.marcar(i))
            b.grid(row=i//3, column=i%3)
            self.botones.append(b)

        self.mensaje = tk.Label(self.root, text='Tu turno' if self.turno == JUGADOR else 'Esperando al otro jugador')
        self.mensaje.grid(row=3, column=0, columnspan=3)

    def marcar(self, i):
        if self.tablero[i] is None and self.turno == JUGADOR:
            valor = 'X' if JUGADOR == 1 else 'O'
            self.actualizar_casilla(i, valor)
            paquete = {'tipo': 'movimiento', 'datos': {'casilla': i, 'valor': valor}}
            self.enviar_callback(json.dumps(paquete))
            self.turno = 3 - JUGADOR
            self.actualizar_mensaje()
            self.verificar_estado()

    def actualizar_casilla(self, i, valor):
        if self.tablero[i] is None:
            self.tablero[i] = valor
            self.botones[i].config(text=valor, state='disabled')
            self.turno = JUGADOR
            self.actualizar_mensaje()
            self.verificar_estado()

    def actualizar_mensaje(self):
        if self.turno == JUGADOR:
            self.mensaje.config(text='Tu turno')
        else:
            self.mensaje.config(text='Esperando al otro jugador')

    def verificar_estado(self):
        combinaciones = [
            (0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)
        ]
        for a,b,c in combinaciones:
            if self.tablero[a] and self.tablero[a] == self.tablero[b] == self.tablero[c]:
                ganador = 'Jugador 1' if self.tablero[a] == 'X' else 'Jugador 2'
                self.mensaje.config(text=f'{ganador} ha ganado!')
                self.deshabilitar_tablero()
                return
        if all(self.tablero):
            self.mensaje.config(text='Empate!')
            self.deshabilitar_tablero()

    def deshabilitar_tablero(self):
        for b in self.botones:
            b.config(state='disabled')

    def iniciar(self):
        self.root.mainloop()
    

# Servidor TCP para recibir movimientos
def servidor(gui):
    def manejar_cliente(conn, addr):
        try:
            data = conn.recv(1024)
            if data:
                paquete = json.loads(data.decode())
                tipo = paquete.get('tipo')
                datos = paquete.get('datos')
                if tipo in funciones:
                    funciones[tipo](gui, datos)
        except:
            pass
        conn.close()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((IP, PUERTO_LOCAL))
    s.listen(5)
    print(f'Servidor escuchando en {IP}:{PUERTO_LOCAL}')
    while True:
        conn, addr = s.accept()
        threading.Thread(target=manejar_cliente, args=(conn, addr), daemon=True).start()

# Cliente TCP para enviar movimientos
def enviar_mensaje(mensaje):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP_REMOTO, PUERTO_REMOTO))
        s.sendall(mensaje.encode())
        s.close()
    except Exception as e:
        print(f'Error al enviar a {IP_REMOTO}:{PUERTO_REMOTO} - {e}')

# Lanzamiento del sistema
if __name__ == '__main__':
    gui = JuegoGato(enviar_mensaje)
    threading.Thread(target=servidor, args=(gui,), daemon=True).start()
    gui.iniciar()
