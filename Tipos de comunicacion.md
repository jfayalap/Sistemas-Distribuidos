# Comunicación en Sistemas Distribuidos

## Índice
- [**Introducción**](#introducción)
- [**Funciones Primitivas de Comunicación**](#funciones-primitivas-de-comunicación)
  - [Características de las Primitivas](#características-de-las-primitivas)
- [**Tipos de Comunicación**](#tipos-de-comunicación)
  - [Comunicación Directa](#comunicación-directa)
  - [Comunicación Indirecta](#comunicación-indirecta)
- [**Comunicación en Grupo**](#comunicación-en-grupo)
  - [Características](#características-de-la-comunicación-en-grupo)
- [**Modos de Difusión**](#modos-de-Difusión)
  - [Comunicación de Difusión](#comunicación-de-difusión)
  - [Comunicación de Multidifusión](#comunicación-de-multidifusión)
  - [Comunicación Unicast](#comunicación-unicast)


## **Introducción**

La **comunicación en sistemas distribuidos** es el proceso mediante el cual dispositivos y procesos independientes dentro de un sistema coordinado comparten información y recursos a través de una red.  
Dado que no existe memoria compartida, la coordinación ocurre mediante **paso de mensajes**, donde los datos se envían directamente de un proceso a otro mediante **procedimientos remotos (RPC)**.


## **Funciones Primitivas de Comunicación**

1. **Envío**
2. **Recepción**
3. **Conexión**
4. **Desconexión**


## **Características de las Primitivas**

### **1. Bloqueantes vs No Bloqueantes**

- **Primitiva bloqueante:** la operación detiene al proceso hasta que se completa.  
- **Primitiva no bloqueante:** la operación no detiene la ejecución y el proceso continúa.

### **2. Sincrónicas vs Asincrónicas**

Aplican principalmente a `send` y `receive`:

- **Envío asincrónico:** el transmisor nunca se bloquea; si la cola está llena, debe reintentar más tarde.  
- **Envío sincrónico:** el transmisor se bloquea hasta que haya espacio para depositar el mensaje.  
- **Recepción asincrónica:** el receptor no se bloquea; si la cola está vacía, debe intentar más tarde.  
- **Recepción bloqueante:** el receptor se bloquea hasta que llegue un mensaje.


## **Tipos de Comunicación**

Los procesos se comunican mediante **intercambio explícito de mensajes**, no compartiendo memoria.

Funciones esenciales:
- `Send(message)`
- `Receive(message)`


## **Comunicación Directa**

El proceso emisor **nombra explícitamente** al receptor:

- `Send(A, message)`  
- `Receive(A, &message)`

<img width="264" height="155" alt="image" src="https://github.com/user-attachments/assets/bd3a8d4c-96cd-4776-94e5-d85d82301070" />


## **Características:

- El enlace se establece automáticamente entre los procesos.  
- Cada enlace conecta **solo dos procesos**.  
- Entre un par de procesos solo existe **un enlace**.


## **Comunicación Indirecta**

Los mensajes se envían a **buzones/puertos**:

- `Send(P, message)`  
- `Receive(P, &message)`

<img width="276" height="221" alt="image" src="https://github.com/user-attachments/assets/319f8ed8-0a11-4c18-93a6-a0da98699074" />


## Características:

- El enlace existe solo si ambos procesos comparten el mismo puerto.  
- Un puerto puede ser compartido por varios procesos.  
- Puede haber múltiples enlaces entre procesos.


## **Comunicación en Grupo**

Un proceso envía mensajes a **un conjunto de procesos**, permitiendo colaboración distribuida.

<img width="337" height="97" alt="image" src="https://github.com/user-attachments/assets/d94f9a25-7af8-4bcb-8294-bd8753a1be2d" />


## Ventajas:

- Abstracción que oculta el paso interno de mensajes.  
- Mejor sincronización entre nodos.  
- Aumento del rendimiento global del sistema.


### **Características de la Comunicación en Grupo**

- **Atomicidad:** si un miembro no recibe el mensaje, el transmisor recibe un error.

## Tipos de orden de mensajes:

- **Sin orden:** no se garantiza un orden específico.  
- **FIFO:** los mensajes se entregan en orden de envío.  
- **Orden causal:** se respetan relaciones de causalidad.  
- **Orden total:** todos ven los mensajes en el mismo orden global.

<img width="298" height="167" alt="image" src="https://github.com/user-attachments/assets/92d11064-e26b-43ae-a90b-5c84fc6dcb71" />



## **Modos de Difusión**

### Comunicación de Difusión (Broadcast)

- Se envía un mensaje simultáneamente a *todos* los procesos.  
- Es rápida porque no requiere procesamiento individual.  
- Limitada en flexibilidad.

<img width="214" height="186" alt="image" src="https://github.com/user-attachments/assets/b3759abf-d8a9-4d7e-82df-cd3a38076810" />



### **Comunicación de Multidifusión (Multicast)**

- El mensaje se envía a un **subconjunto específico** de procesos.  
- Ideal para cargas altas.  
- Reduce el tiempo de manejo de mensajes.

<img width="165" height="153" alt="image" src="https://github.com/user-attachments/assets/9ac8c056-745e-4acf-9017-fdf05f54e6bc" />


### **Comunicación Unicast**

- Comunicación **uno a uno** entre procesos.  
- Ideal para interacciones directas.  
- Enfoque simple y eficiente.

<img width="164" height="122" alt="image" src="https://github.com/user-attachments/assets/36ee2901-c97c-4784-831e-263d328b890e" />


