import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# Definir los nodos P2P
nodos = [
    ('127.0.0.1', 10000),
    ('127.0.0.1', 11000),
    ('127.0.0.1', 12000),
    ('127.0.0.1', 13000)
]

# en este caso el nodo inicial lo hare 2 veces, donde el valor del nodo inicial
#sera diferente en cada ocasion 

nodo_inicial = 1
IP, PUERTO_LOCAL = nodos[nodo_inicial]

# Interfaz gráfica
class Interfaz:
    def __init__(self, enviar_callback):
        self.root = tk.Tk()
        self.root.title(f'Chat P2P - Nodo {nodo_inicial + 1}')
        
        self.chat_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, state='disabled')
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        self.entry = tk.Entry(self.root)
        self.entry.pack(padx=10, pady=5, fill=tk.X)
        self.entry.bind('<Return>', lambda event: self.enviar())
        
        self.enviar_callback = enviar_callback

    def enviar(self):
        mensaje = self.entry.get()
        self.entry.delete(0, tk.END)
        if mensaje:
            self.enviar_callback(mensaje)
            self.mostrar_mensaje(f'Yo: {mensaje}')
    
    def mostrar_mensaje(self, mensaje):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, mensaje + '\n')
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)

    def iniciar(self):
        self.root.mainloop()

# Servidor TCP 
def servidor(gui):
    def manejar_cliente(conn, addr):
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break
                mensaje = data.decode()
                gui.mostrar_mensaje(f'{addr[0]}:{addr[1]} dice: {mensaje}')
            except:
                break
        conn.close()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  
    s.bind((IP, PUERTO_LOCAL))
    s.listen(5)
    print(f'Servidor escuchando en {IP}:{PUERTO_LOCAL}')
    while True:
        conn, addr = s.accept()
        threading.Thread(target=manejar_cliente, args=(conn, addr), daemon=True).start()

# Cliente TCP para enviar mensajes
def enviar_mensaje(mensaje):
    for ip, puerto_remoto in nodos:
        if (ip, puerto_remoto) != (IP, PUERTO_LOCAL):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, puerto_remoto))
                s.sendall(mensaje.encode())
                s.close()
            except Exception as e:
                print(f'Error al enviar a {ip}:{puerto_remoto} - {e}')

# Lanzamiento del sistema
if __name__ == '__main__':
    gui = Interfaz(enviar_mensaje)
    threading.Thread(target=servidor, args=(gui,), daemon=True).start()
    gui.iniciar()
