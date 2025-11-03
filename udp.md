# Comunicación de Protocolo de Datagrama de Usuarios (UDP) 
------

Es un protocolo que transmite datos de forma rápida y eficiente sin la necesidad de establecer una conexión previa. 
Esto es idea par aplicaciones como streamings de videos, juegos en linea. Sin embargo, la ausencia de una conexión, provocando una ausencia en la garantía de entrega de todos los paquetes ya que prioriza la velocidad y minimiza la latencia.

## Características principales de la comunicación UDP 
------
 



| Caracteristica | UDP  | TCP |
|------|--------------|--------|
|Conexion | Sin Conexion | Establece una conexion antes de la comunicación
|Fiabilidad | No es garantizada | Garantizada |
|Velocidad | Más rápido | Es más lento debido a la sobrecarga de la Conexion|
|Usos| Streaming, juegos en línea | transferencia de archivos, sitios web | 


Para ver más sobre el protocolo TCP protocolo puedes leer https://github.com/jfayalap/Sistemas-Distribuidos/blob/main/tcp_server_client.md 

<img width="522" height="244" alt="Screenshot 2025-11-02 at 3 59 50 PM" src="https://github.com/user-attachments/assets/8b446ee1-f5ba-419d-9c84-fd9e0e03916c" />

## Ventajas de la conexión UDP 
------

Este tipo de conexión es muy eficiente debido a la sobrecarga mínima que se usa, ya que se usa menos recursos con respecto al protocolo TCP, ademas permite, enviar datos a varios receptores de manera simultánea.

Ya que no es necesario una conexión antes de enviar datos, la Transmisión es mas rápida y con menor retraso, lo cual esto es muy eficiente para aplicaciones donde el tiempo es indispensable. 

## Desventajas  de la conexión UDP 
------

Uno de los mayores problemas es la falta de confiabilidad dado que es muy sencillo que se pierdan los paquetes y seguridad de la misma, debido a que no existen mecanismos de autenticidad. 

UDP no tiene mecanismos para gestionar el tráfico de red, por lo que es muy sencillo saturar la red y generar errores. 


