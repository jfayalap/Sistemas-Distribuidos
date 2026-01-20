# Transacción

- Una transacción se define como una secuencia de operaciones del servidor que garantiza que será atómica en presencia de múltiples clientes y caídas del servidor.
- Estas transacciones abarcan varios nodos o sistemas, ejecutándose como una sola unidad lógica para garantizar la consistencia de los datos.
- Estas transacciones siguen las propiedades **ACID** (Atomicidad, Consistencia, Aislamiento y Durabilidad).
- Las transacciones se estructuran a partir de conjuntos de otras transacciones, las cuales son particularmente útiles porque permiten una concurrencia adicional.

---

# Concurrencia

- Es la capacidad de múltiples componentes o nodos de ejecutar tareas y procesos de manera simultánea, compartiendo recursos y comunicándose a través de una red para alcanzar un objetivo.
- Esto permite que los sistemas sean más eficientes y fiables, ya que permite manejar grandes volúmenes de datos y tareas complejas.

## Características de la concurrencia en sistemas distribuidos
1. **Ejecución simultánea**: diferentes tareas o procesos se ejecutan al mismo tiempo en distintos nodos del sistema.  
2. **Comunicación por mensajes**: los nodos independientes se comunican entre sí pasando mensajes para coordinar sus acciones.  
3. **Independencia de componentes**: cada componente puede fallar sin afectar a los demás, lo que aumenta la fiabilidad del sistema.  
4. **Ausencia de reloj global**: implica la necesidad de mecanismos de sincronización para coordinar acciones entre nodos.  

---

## Desafíos de la concurrencia
1. **Inconsistencia de datos**: la manipulación simultánea puede provocar resultados incorrectos si no se controla adecuadamente el acceso.  
2. **Fallos en los nodos**: se requieren mecanismos de recuperación y tolerancia a fallos, dado que cada componente puede fallar.  
3. **Conflictos de acceso**: múltiples tareas que intentan modificar el mismo dato o recurso al mismo tiempo pueden entrar en conflicto.  

---

## Mecanismos y técnicas para el control de concurrencia
1. **Bloqueos (Locks)**: impiden que otros procesos accedan a un recurso mientras uno lo está utilizando.  
2. **Semáforos**: herramienta de sincronización que gestiona el acceso a recursos compartidos por un número limitado de procesos.  
3. **Control de concurrencia multiversión (MVCC)**: mantiene múltiples versiones de los datos, permitiendo que las transacciones se realicen sin bloquearse mutuamente y asegurando la consistencia de las versiones.  
4. **Replicación**: mantenimiento de múltiples copias de datos y/o servicios en diferentes nodos para mejorar la disponibilidad y rendimiento.  
