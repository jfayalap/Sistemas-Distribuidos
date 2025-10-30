# Arquitectura cliente - servidor 
------

Es un modelo de software en el que las tareas se reparten entre los proveedores de recursos o servicios, llamados servidores y, los que piden la informacion clientes. En este tipo de arquitectura, la capacidad de proceso se encuentra repartida entre los clientes y los servidores. 
Por otro lado, la red cliente-servidor, es una red de comunicacion en la cual los clientes se encuentran conectados a un servidor, en el que se centra en los recursos. 


## Componentes clave: 
----

Cliente: Es la parte que inica las peticiones de servidores hacia el servidor, usando la red como el mecanismo de comunicación. El vliente envía una petición al servidor web y, el mismo servidor, es el que devuelve los datos solicitados mediante peticiones HTTP. 


Servidor: Se encarga de proporcionar los servicicios a los clientes. Puede consistir en distintos compoentnes del software, también, es un harware que proporciona los recursos necesario para otros ordenadores y/o programas. El servidor siempre acepta las peticiones del cliente, las procesa y proporciona una respuesta. 

## Cómo funciona: 
----

•	El cliente solicita un servicio: el cliente inicia una solocitud a un servicio (ya sea en su computadora, tableta y/o teléfono).

•	El servidor procesa la solicitud: el servidor recibe la petición, la procesa y busca la información para después ejecutar la tarea solicitada. 

•	El servidor responde: una vez procesado, el servidor envía los datos de vuelta al cliente. 

•	El cliente recibe y muestra: el cliente recibe la respuesta y presenta la información de manera amigable al usuario: 


<img width="931" height="655" alt="Screenshot 2025-10-27 at 1 03 58 PM" src="https://github.com/user-attachments/assets/7dbd54ed-8247-4a78-8c6e-1da160aa0f00" />


## Ventajas: 
----

•	Simplificación de los datos ya que se gestionan desde un único punto (el servidor).

•	Los datos sensisbles se pueden proteger con medidas de seguridad sólidas.

•	Es más sencillo mejorar el rendimiento del servidor sin interrumpir el servicio principal. 

•	Los datos se almacenan en un lugar centralizado, permitiendo mantener la coherencia y evita el duplicado de datos. 

## Ejemplo: 
----

El siguiente ejemplo es una conexión entre cliente-servidor, donde el servidor recibe el mensaje Hola Mundo, siempre y cuando el cliente ingresa IP y el puerto igual al del servidor, de lo contrario, no se envia ningun mensaje. 

El código lo puedes encontrar aqui : 

https://github.com/jfayalap/Sistemas-Distribuidos/blob/main/tcp_server_client.py

## Captura de pantalla del código cliente 
<img width="321" height="57" alt="Screenshot 2025-10-30 at 12 31 27 PM" src="https://github.com/user-attachments/assets/130d87fb-51b3-4740-ba93-932357bbf9e4" />


## Captura de pantalla del código servidor 
<img width="381" height="55" alt="Screenshot 2025-10-30 at 12 31 38 PM" src="https://github.com/user-attachments/assets/016f695b-399c-4abe-aef9-f9f85cc8019d" />
