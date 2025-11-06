# 📡 Comunicación de Protocolo de Datagrama de Usuarios (UDP)

Este documento explica el funcionamiento del protocolo UDP, sus características, ventajas y desventajas, comparándolo con TCP. Ideal para estudiantes y desarrolladores que trabajan con sistemas distribuidos y aplicaciones en tiempo real.

---

## 📑 Índice

- [¿Qué es UDP?](#qué-es-udp)
- [Características principales de UDP](#características-principales-de-udp)
- [Comparación UDP vs TCP](#comparación-udp-vs-tcp)
- [Ventajas de UDP](#ventajas-de-udp)
- [Desventajas de UDP](#desventajas-de-udp)
- [Más sobre TCP](#más-sobre-tcp)

---

## ❓ ¿Qué es UDP?

El **Protocolo de Datagrama de Usuario (UDP)** transmite datos de forma rápida y eficiente sin necesidad de establecer una conexión previa.  
Es ideal para aplicaciones como streaming de video y juegos en línea.  
Sin embargo, al no establecer conexión, no garantiza la entrega de todos los paquetes, ya que prioriza la velocidad y minimiza la latencia.

---

## ⚙️ Características principales de UDP

UDP se caracteriza por su simplicidad y rapidez, pero también por su falta de mecanismos de control y fiabilidad.

---

## 📊 Comparación UDP vs TCP

| Característica | UDP | TCP |
|----------------|-----|-----|
| Conexión       | Sin conexión | Establece conexión previa |
| Fiabilidad     | No garantizada | Garantizada |
| Velocidad      | Más rápido | Más lento por sobrecarga |
| Usos           | Streaming, juegos en línea | Transferencia de archivos, sitios web |

---

## 🚀 Ventajas de UDP

- Baja sobrecarga: utiliza menos recursos que TCP.
- Transmisión rápida: no requiere conexión previa.
- Multicast: permite enviar datos a varios receptores simultáneamente.
- Ideal para aplicaciones sensibles al tiempo como videollamadas, transmisiones en vivo y juegos.

---

## ⚠️ Desventajas de UDP

- Falta de confiabilidad: los paquetes pueden perderse fácilmente.
- Sin autenticación: no hay mecanismos de seguridad integrados.
- Saturación de red: no gestiona el tráfico, lo que puede causar errores.

---

## 📎 Más sobre TCP

Para ver más sobre el protocolo TCP, consulta el siguiente archivo del repositorio:  
👉 [tcp_server_client.md](https://github.com/jfayalap/Sistemas-Distribuidos/blob/main/tcp_server_client.md)

---

## 🖼️ Ejemplo visual

![UDP vs TCP](https://github.com/user-attachments/assets/8b446ee1-f5ba-419d-9c84-fd9e0e03916c)

---

