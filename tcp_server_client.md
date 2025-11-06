# 🖥️ Arquitectura Cliente-Servidor

Este documento explica el modelo cliente-servidor, sus componentes, funcionamiento, ventajas y un ejemplo práctico con código en Python. Es útil para entender cómo se estructuran muchas aplicaciones distribuidas modernas.

---

## 📑 Índice

- [¿Qué es la arquitectura cliente-servidor?](#qué-es-la-arquitectura-cliente-servidor)
- [Componentes clave](#componentes-clave)
  - [Cliente](#cliente)
  - [Servidor](#servidor)
- [Cómo funciona](#cómo-funciona)
- [Ventajas](#ventajas)
- [Ejemplo práctico](#ejemplo-práctico)
  - [Captura del código cliente](#captura-del-código-cliente)
  - [Captura del código servidor](#captura-del-código-servidor)

---

## ❓ ¿Qué es la arquitectura cliente-servidor?

Es un modelo de software en el que las tareas se reparten entre los proveedores de recursos o servicios (servidores) y los que solicitan información (clientes).  
La capacidad de procesamiento se distribuye entre ambos, y la red cliente-servidor conecta múltiples clientes a un servidor centralizado que gestiona los recursos.

---

## 🧩 Componentes clave

### Cliente

Es la parte que inicia las peticiones hacia el servidor, usando la red como mecanismo de comunicación.  
El cliente envía una solicitud al servidor web, y este devuelve los datos solicitados mediante peticiones HTTP.

### Servidor

Se encarga de proporcionar servicios a los clientes.  
Puede consistir en componentes de software, y también en hardware que ofrece recursos a otros ordenadores o programas.  
El servidor acepta las peticiones del cliente, las procesa y proporciona una respuesta.

---

## 🔄 Cómo funciona

1. **El cliente solicita un servicio:** desde una computadora, tableta o teléfono.
2. **El servidor procesa la solicitud:** busca la información y ejecuta la tarea.
3. **El servidor responde:** envía los datos de vuelta al cliente.
4. **El cliente recibe y muestra:** presenta la información de forma amigable al usuario.

![Diagrama cliente-servidor](https://github.com/user-attachments/assets/7dbd54ed-8247-4a78-8c6e-1da160aa0f00)

---

## ✅ Ventajas

- Simplificación de los datos al gestionarse desde un único punto.
- Protección de datos sensibles mediante medidas de seguridad sólidas.
- Mejora del rendimiento del servidor sin interrumpir el servicio.
- Almacenamiento centralizado que evita duplicación y mantiene coherencia.

---

## 🧪 Ejemplo práctico

Este ejemplo muestra una conexión cliente-servidor en Python.  
El servidor recibe el mensaje "Hola Mundo" solo si el cliente usa la misma IP y puerto.  
De lo contrario, no se envía ningún mensaje.

📄 Código fuente:  
👉 [tcp_server_client.py](https://github.com/jfayalap/Sistemas-Distribuidos/blob/main/tcp_server_client.py)

---

### 🖼️ Captura del código cliente

![Código cliente](https://github.com/user-attachments/assets/130d87fb-51b3-4740-ba93-932357bbf9e4)

---

### 🖼️ Captura del código servidor

![Código servidor](https://github.com/user-attachments/assets/016f695b-399c-4abe-aef9-f9f85cc8019d)

---
