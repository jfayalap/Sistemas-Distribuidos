# 🧠 Suite de Protocolos y Topologías en Sistemas Distribuidos


---

## 📚 Índice

1. [Suite de protocolos TCP/IP](#suite-de-protocolos-tcpip)
2. [Capas del modelo TCP/IP](#capas-del-modelo-tcpip)
3. [Proceso de comunicación TCP/IP](#proceso-de-comunicación-tcpip)
4. [Topología de red](#topología-de-red)
   - [Topologías físicas](#topologías-físicas)
   - [Topologías lógicas](#topologías-lógicas)
5. [Autor y consultoría](#autor-y-consultoría)

---

## 🔗 Suite de protocolos TCP/IP

Una **suite de protocolos** es un conjunto de reglas que trabajan en conjunto para permitir la comunicación entre dispositivos en red.

- La suite **TCP/IP** es un estándar abierto, disponible sin costo.
- Es la base de Internet y redes modernas.

---

## 🧩 Capas del modelo TCP/IP

![Modelo TCP/IP](https://static.platzi.com/media/user_upload/Captura%20de%20Pantalla%202022-01-26%20a%20la(s)%205.30.22%20p.m.-8d0a2556-7853-45b8-b910-7cc4aa4ab30f.jpg)

1. **Capa de aplicación**  
   Protocolos como `HTTP`, `DNS`.

2. **Capa de transporte**  
   Comunicación entre aplicaciones (`TCP`, `UDP`).

3. **Capa de internet**  
   Enrutamiento de paquetes (`IPv4`, `IPv6`).

4. **Capa de acceso a la red**  
   Comunicación local (`Ethernet`, `Wi-Fi`).

---

## 🔄 Proceso de comunicación TCP/IP

![Encapsulamiento TCP/IP](https://ccnadesdecero.es/wp-content/uploads/2020/01/Capas-del-modelo-TCP-IP.jpg)

- **TCP** garantiza la entrega ordenada y completa.
- **IP** gestiona el direccionamiento y enrutamiento.

### 🔃 Encapsulamiento (Servidor → Cliente)

1. El servidor prepara la página HTML.
2. `HTTP` envía los datos a la capa de transporte.
3. `TCP` divide los datos en segmentos.
4. `IP` encapsula los segmentos en paquetes.
5. `Ethernet` crea la trama y la envía al router.

### 🔃 Desencapsulamiento (Cliente)

1. Se elimina el encabezado de `Ethernet`.
2. Se elimina el encabezado de `IP`.
3. Se elimina el encabezado de `TCP`.
4. El navegador procesa la información `HTTP`.

---

## 🌐 Topología de red

La **topología** define cómo se conectan y comunican los dispositivos en una red.

---

### 🛠️ Topologías físicas



1. **Estrella**:

•	Los nodos estan conectados a un concentrador central

•	Este tipo de topologia facilita la resolucion de problemas en un nodo particular, si un nodo falla el resto de la red no se ve afectada. 

2.  **Bus**: 

•	Todos los dispositivos comparten un unico cable principal 

•	Dificil de diagnosticar fallos

•	Si el cable principal falla, toda la red se ve afectada

•	La informacion viaja por el cable  en ambos y tiene en sus dos extremos una resistencia llamada terminador. 

3. **Anillo**: 

•	Cada dispositivo esta conectado al siguiente, formando un circulo cerrado

•	Los datos circulan en una direccion 

•	Si un nodo falla, puede interrumpir toda la red.

•	Este tipo de comunicación se da por el paso de un token 

4. **Malla**: 

•	Cada dispositivo (nodo) esta conectado a todos los demas nodos 

•	Cada servidor tiene sus propias conexiones con todos los demas servidores

•	La red puede funcionar aun cuando un nodo desaparece y/ la conexión falla ya que el resto de los nodos evitan el paso por este punto 

5. **Híbrida**: Combinación de topologías.

•	Combinacion de dos topologías. 

6. **Punto a punto (P2P)**:

•	Es un enlace permanente entre dos puntos finales conocidos como punto a punto (P2P). 

•	El valor de una red permanente de P2P es la comunicación sin obstaculos entre los dos puntos finales

7. **Árbol**: 

•	Consiste en un conjunto de subredes estrella conectadas a un bus, facilitando el crecmiento de la red.

•	Esta compuesta por un cableado punto a punto 

•	Si se viene abajo el segmento principal, todo el segmento se viene abajo con el

8. **Fully connected**: Alta confiabilidad, alto costo.

•	Las redes disenadas suelen ser muy caras de configurar pero dan un alto grado de confiabilidad 

---

### 🧭 Topologías lógicas



1. **Lógica en bus**: Todos los nodos comparten el canal.
2. **Lógica en anillo**: Datos circulan en una sola dirección.
3. **Lógica en estrella**: Comunicación a través de un nodo central.
4. **Lógica en malla**: Múltiples rutas posibles para los datos.

---

## 👨‍💻 Autor y consultoría

Este contenido forma parte de mi portafolio como **Cloud Test Engineer en transición hacia Data Engineer**.  
Ofrezco **consultoría técnica para PYMEs** en Tijuana y Latinoamérica, enfocada en:

- Calidad de datos
- Arquitectura distribuida
- Documentación profesional

🔗 Repositorio completo: [Sistemas Distribuidos](https://github.com/jfayalap/Sistemas-Distribuidos)

---
