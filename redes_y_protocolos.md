# 📡 Redes y Protocolos

Este documento explica los conceptos clave sobre redes, protocolos de comunicación y mecanismos de sincronización y manejo de errores en sistemas distribuidos.

---

## 📑 Índice

- [Redes y Protocolos](#redes-y-protocolos)
- [Protocolos de Comunicación](#protocolos-de-comunicación)
  - [1. Sintaxis](#1-sintaxis)
  - [2. Semántica](#2-semántica)
  - [3. Sincronización](#3-sincronización)
  - [4. Manejo de Errores](#4-manejo-de-errores)
- [Ejemplos Comunes de Protocolos](#ejemplos-comunes-de-protocolos)

---

## 🌐 Redes y Protocolos

Las redes son sistemas de dispositivos interconectados para compartir información, mientras que los protocolos son las reglas que permiten a estos dispositivos comunicarse de manera eficiente y fiable.

Los protocolos permiten que equipos con diferentes arquitecturas se entiendan y colaboren como si hablaran un lenguaje común.

---

## 🔁 Protocolos de Comunicación

Conjunto de reglas y procedimientos que dictan cómo deben comunicarse los dispositivos en una red.

### 1. Sintaxis

Define el formato, estructura y codificación de los mensajes para asegurar que los datos sean legibles.

**Elementos clave:**

- **Formato de datos:** Organización de bits y bytes.
- **Estructura del mensaje:** Encabezados y cuerpos.
- **Codificación de datos:** Representación comprensible para el receptor.

**Ejemplos:**

- `HTTP`: Sintaxis definida para solicitudes y respuestas.
- `SIP`: Protocolo de inicio de sesión con estructura específica.

<img width="322" height="102" alt="image" src="https://github.com/user-attachments/assets/66876e5b-fa54-4c90-943c-2b19a4604826" />


---

### 2. Semántica

Se refiere al significado de los comandos y datos, y cómo se interpretan correctamente.

**Incluye:**

- **Interpretación de datos**
- **Coordinación de acciones**
- **Gestión de errores**



<img width="364" height="90" alt="image" src="https://github.com/user-attachments/assets/a27f6e11-e3a6-4dcf-bdbd-4040dd58f43c" />

> Ejemplo: En este ejemplo podemos ver que, la sintaxis si esta bien porque es un codigo bien hecho, sin embargo, no cuenta con una buena semantica ya que no se puede dividir entre cero 
---

### 3. Sincronización

Alineación temporal de dispositivos para operar de forma coordinada.

**Protocolos comunes:**

- `NTP`: Sincronización con precisión de milisegundos.
- `PTP`: Alta precisión para aplicaciones críticas.
- `SyncE`: Sincronización en redes Ethernet.

<img width="395" height="366" alt="image" src="https://github.com/user-attachments/assets/a3de7197-ce29-4797-a6f2-f3d6b01b1b28" />


**Otros usos:**

- `MIDI`, `DMX`: Sincronización de eventos audiovisuales.

---

### 4. Manejo de Errores

Mecanismos para detectar y corregir fallos durante la transmisión de datos.

#### Detección de errores

- **Bit de paridad**
- **CRC (Código de Redundancia Cíclica)**
- **Suma de verificación**

#### Corrección de errores

- **Retransmisión**
- **CCE (Códigos de Corrección de Errores)**

---

## 📦 Ejemplos Comunes de Protocolos

- `IP`: Direccionamiento de paquetes.
- `HTTP`: Transferencia de datos web.
- `DNS`: Traducción de nombres de dominio.
- `SMTP`: Envío de correos electrónicos.
- `Ethernet`: Comunicación física en redes.
- `TLS`: Cifrado y seguridad de datos.

---

