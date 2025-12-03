# 📘 Índice

1. [¿Qué es RMI?](#qué-es-rmi)  
   1.1 [Cómo funciona RMI](#cómo-funciona-rmi)  
   1.2 [Consideraciones al usar RMI](#consideraciones-al-usar-rmi)  

2. [Network File System (NFS)](#network-file-system-nfs)  
   2.1 [Sistema de archivos distribuidos](#sistema-de-archivos-distribuidos)  
   2.2 [Diseño del sistema de archivos de red NFS: protocolo sin estado](#diseño-del-sistema-de-archivos-de-red-nfs-protocolo-sin-estado)  

3. [ONC RPC (Open Network Computing Remote Procedure Call)](#onc-rpc-open-network-computing-remote-procedure-call)  
   3.1 [Componentes principales](#componentes-principales)  
   3.2 [Funcionamiento](#funcionamiento)  

---

# ¿Qué es RMI?

- Es un mecanismo de programación orientada a objetos que permite que un objeto en una aplicación llame a un método en un objeto que reside en otra máquina virtual de Java o computadora a través de la red.  
- RMI facilita la creación de aplicaciones distribuidas al permitir la interacción entre objetos en diferentes ubicaciones, utilizando componentes como *stubs* y *esqueletos* para gestionar la comunicación remota.  

## Cómo funciona RMI

- **Cliente**: un objeto cliente invoca un método como si fuera local.  
- **Stub**: proxy que actúa en nombre del objeto remoto en el lado del cliente.  
- **Esqueleto (servidor proxy)**: recibe la llamada desde el stub, desempaqueta los argumentos y ejecuta el método real en el objeto remoto.  
- **Resultado**: el objeto remoto ejecuta el método y devuelve el resultado al cliente a través del esqueleto y el stub.  

## Consideraciones al usar RMI

- No garantiza invocaciones en diferentes hilos de ejecución → se requieren excepciones *thread-safe*.  
- El algoritmo de recolección de basura distribuido interactúa con el recolector de la VM local.  
- RMI por defecto usa el protocolo RMI, pero puede cambiarse a HTTP/HTTPS y modificar el puerto.  
- El puerto estándar es **1099**.  


<img width="279" height="113" alt="image" src="https://github.com/user-attachments/assets/0ab0d957-5851-48e1-b341-6a0e05d2dbd2" />



<img width="314" height="70" alt="image" src="https://github.com/user-attachments/assets/7b554894-891b-467b-93f4-bd1a593c95a0" />


---

# Network File System (NFS)

- Es un protocolo de sistema de archivos distribuido.  
- Es abierto, lo que permite que terceros escriban sus propias implementaciones.  


<img width="426" height="215" alt="image" src="https://github.com/user-attachments/assets/cafefb83-8dcd-4498-ad14-94339344a82a" />

## Sistema de archivos distribuidos

- Uno o varios servidores atienden a múltiples clientes.  
- El servidor almacena datos en disco y los clientes acceden a ellos vía red.  
- Cliente y servidor contienen el sistema de archivos, permitiendo lectura/actualización como si fuera local.  
- El cliente envía solicitudes al servidor, recibe respuestas y las guarda en su búfer local para reducir tráfico de red.  

## Diseño del sistema de archivos de red NFS: protocolo sin estado

- Se basa en **identificadores de archivo**, que constan de:  
  - **Identificador de volumen**: identifica el volumen en disco.  
  - **Número de inodo**: especifica el archivo dentro del volumen.  
  - **Número de generación**: asegura unicidad del archivo.  

---

# ONC RPC (Open Network Computing Remote Procedure Call)

- Marco de software de **Sun Microsystems** que permite ejecutar funciones en otro sistema como si fueran locales.  
- Utiliza la familia de protocolos **TCP/IP** y fue diseñado para aplicaciones cliente-servidor distribuidas y heterogéneas.  

## Componentes principales

- **Remote Procedure Call (RPC)**: protocolo que permite ejecutar procedimientos en otra máquina.  
- **Open Network Computing (ONC)**: marco de código abierto para redes abiertas.  
- **TCP/IP**: base de comunicación de ONC RPC.  
- **Portmapper**: servicio que registra procedimientos y dirige clientes a los puertos correctos.  

## Funcionamiento

1. **Registro del servicio**: el servidor registra procedimientos con el portmapper.  
2. **Búsqueda del cliente**: el cliente solicita la dirección del procedimiento al portmapper.  
3. **Llamada remota**: el cliente invoca el procedimiento en el servidor.
4. **Ejecución**: el servidor ejecuta el procedimiento.  
5. **Retorno del resultado**: el servidor devuelve el resultado al cliente como si fuera local.

<img width="705" height="366" alt="Screenshot 2025-12-02 at 8 58 43 PM" src="https://github.com/user-attachments/assets/7b053e21-6b39-4de3-b7fc-cdbb9fc1a538" />
