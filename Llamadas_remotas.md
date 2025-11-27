# Métodos de llamadas Remotas (RPC)

# Índice

1. [Métodos de llamadas Remotas (RPC)](#métodos-de-llamadas-remotas-rpc)
2. [Modelo RPC](#modelo-rpc)
3. [Arquitectura RPC](#arquitectura-rpc)
   - [Elementos clave de la arquitectura RPC](#elementos-clave-de-la-arquitectura-rpc)
4. [Funcionamiento de una llamada RPC](#funcionamiento-de-una-llamada-rpc)


- Fue creada en Java y es enfocada para lenguajes de programación que usan Programación Orientada en Objetos.  
- Permite el empaquetado y recepción de objetos mediante comunicación con una o varias *virtual machines*.  
- Son un protocolo que permite a un programa informático ejecutar un procedimiento o función en otro ordenador o servidor, como si fuera una llamada a una función local, simplificando el desarrollo de aplicaciones distribuidas.  
- RPC presupone la existencia de un protocolo de transporte de bajo nivel como **TCP/IP** o **UDP** para transportar los datos de mensaje entre programas.  
- El protocolo permite a los usuarios trabajar con procedimientos remotos como si los procedimientos fueran locales.  
- Un **cliente** es un sistema o proceso que accede a los servicios o recursos de otro proceso o sistema de la red, mientras que el **servidor** es un sistema que proporciona servicios y recursos que implementa servicios de red.  
- La interfaz RPC se utiliza para comunicarse entre procesos en diferentes estaciones de trabajo de una red.  

---

## Modelo RPC

- RPC cuenta con un hilo de control que serpentea lógicamente a través de dos procesos:  
  - **Proceso del llamante**: envía un mensaje de llamada que incluye los parámetros de procedimiento al proceso de servidor.  
  - **Proceso de servidor**: extrae los parámetros del procedimiento, calcula los resultados y envía un mensaje de respuesta.  

![Modelo RPC](https://github.com/user-attachments/assets/d5e00136-fa14-4f64-981b-99ad522a2466)

- RPC cae en algún lado entre la capa de transporte y de aplicación, debido a que RPC le oculta a la capa de aplicación los detalles de la red.  

---

## Arquitectura RPC

- La arquitectura permite que un programa invoque una función o procedimiento en otro proceso, incluso en una máquina diferente sin que el programador tenga que gestionar los detalles de la comunicación de la red.  
- La arquitectura suele implicar un **middleware** o un **framework** que maneja la serialización, transporte y la interpretación de las llamadas, permitiendo la comunicación entre diferentes sistemas y microservicios.  

### Elementos clave de la arquitectura RPC

- **Cliente**: aplicación que inicia la llamada al procedimiento remoto.  
- **Servidor**: aplicación que contiene el procedimiento que se va a ejecutar en una máquina remota.  
- **Stub (servidor)**: bloque de código en el lado del servidor que representa el procedimiento remoto. Este stub recibe la llamada remota y llama a la implementación real del procedimiento.  
- **Stub (cliente)**: bloque de código en el lado del cliente que representa el procedimiento remoto. Se encuentra en el espacio de direcciones del cliente y actúa como un proxy para el procedimiento en el servidor.  
- **Middleware de red (RPC Runtime)**: parte de la arquitectura que se encarga de toda la comunicación de red:  
  - **Serialización/Des-serialización**: empaquetar los parámetros de la llamada y de la respuesta.  
  - **Transporte**: enviar los datos a través de la red usando protocolos como TCP/IP o HTTP.  

---

## Funcionamiento de una llamada RPC

1. **Llamada al procedimiento**: el cliente llama al procedimiento remoto a través de su stub.  
2. **Serialización**: el stub del cliente serializa los parámetros de la llamada a un formato que se puede enviar a través de la red.  
3. **Transporte**: el stub del cliente envía los datos serializados al stub del servidor a través de la red.  
4. **Des-serialización**: el stub del servidor recibe los datos, los des-serializa y llama a la implementación real del procedimiento remoto.  
5. **Ejecución del procedimiento**: el procedimiento se ejecuta en el servidor.  
6. **Serialización del resultado**: el resultado del procedimiento se serializa de nuevo para ser enviado de regreso al cliente.  
7. **Respuesta al cliente**: el stub del servidor envía el resultado serializado al stub del cliente.  
8. **Des-serialización y devolución**: el stub del cliente des-serializa el resultado y lo devuelve al programa llamador como si fuera una función local.  
