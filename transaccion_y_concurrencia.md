**Transacción** 


•	Una transaccion se define como una secuencia de operaciones del servidor que garantiza que sera atomica en presencia de multiples clientes y caidas del servidor .
•	Estas transacciones abarcan varios nodos o sistemas, ejecutandose como una sola unidad logica para garantizar la consistencia de los datos. 
•	Estas transacciones siguen las propiedades ACID (Atomicidad, Consistencia, Aislamiento y Durabilidad) 
•	Las transacciones se estructuran a partir de conjuntos de otras transacciones, las cuales, son particualrmente utiles porque permiten una concurrencia adicional. 

**Concurrencia**

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
