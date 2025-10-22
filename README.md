# Sistemas-Distribuidos

•	Un sistema distribuido es aquel en el que los componentes (hardware o software) ubicados en computadoras estan conectadas a una red y se comunican y/o coordinan mediante el intercambio de mensajes. 

•	Es un conjunto de computadores independientes que estan interconectados a traves de una red y con la capacidad para realizar una tarea. Las telecomunicaciones permiten la conectividad de un gran numero de usuarios ubicados en cualquier parte del mundo por medio de la transmision de voz, datos y/o video, a traves de una gran variedad de dispositivos. 

<img width="714" height="615" alt="Screenshot 2025-10-21 at 8 26 22 PM" src="https://github.com/user-attachments/assets/bf3c4eaf-10bc-450f-a3d0-2ce68c959c19" />

Concurrencia:

•	Es la capacidad de multiples componentes o nodos de ejecutar tareas y procesos de manera simultanea, compartiendo recursos y comunicandose a traves de una red para alcanzar un objetivo.
•	Esto permite que los sistemas sean mas eficientes y fiables, ya que permite manejar grandes volumenes de datos y tareas complejas.

Caracteristicas de la concurrencia en sistemas distribuidos:

1)	Ejecucion simultanea:   es cuando diferentes tareas o procesos se ejecutan al mismo tiempo en distintos nodos del sistema 
2)	Comnucacion por mensajes: los nodos independientes se comunican entre si pasando mensajes para coordinar sus acciones. 
3)	Independencia de componentes: cada componente puede fallar sin afectar a los demas, lo que aumenta la fiabilidad del sistema. 
4)	No cuenta con un reloj global: La ausencia de un reloj centralizado implica la necesidad de mecanismos de sincronizacion para coordinar acciones entre nodos. 

Desafios de la concurrencia:

1)	Inconsistencia de datos: Dado que la manipulacion de los datos es de manera simultanea, esto puede provocar que los resultados sean incorrectos si no se controla de manera adecuada el acceso. 
2)	Fallos en los nodos: se requiere mecanismos de recuperacion y tolerancia a fallos, dado que cada componente puede fallar. 
3)	Conflictos de acceso: multiples tareas que intentan modificar el mismo dato o recurso al mismo tiempo pueden entrar en conflicto. 


Mecanismos y tecnicas para el control de concurrencia: 

1)	Bloqueos (Locks): mecanismos que impiden que otros procesos accedan a un recurso mientras uno se esta utilizando. 
2)	Semaforos: Herramienta de sincronizacion que permite gestionar el acceso a recursos compartidos por un numero limitado de procesos. 
3)	Control de concurrencia multiversion (MVCC): mantiene multiples versiones de los datos, permitiendo que las transacciones se realicen sin bloquearse mutuamente y asegurando la consistencia de las versiones. 
4)	Replicacion: mantenimiento de multiples copias de datos y/o servicios en diferentes nodos para mejorar la disponibilidad y rendimiento. 


