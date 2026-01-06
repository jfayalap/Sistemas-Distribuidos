# 📘 Índice

1. [**Seguridad y encriptación en sistemas distribuidos**](#seguridad-y-encriptación-en-sistemas-distribuidos)  
   1.1 [**Aspectos clave de la seguridad**](#aspectos-clave-de-la-seguridad)  
   1.2 [**Encriptación**](#encriptación)  
   1.3 [**Tipos de encriptado**](#tipos-de-encriptado)  
   1.4 [**Riesgos y amenazas**](#riesgos-y-amenazas)  

---

# **Seguridad y encriptación en sistemas distribuidos**

La seguridad y encriptación en sistemas distribuidos protege datos y recursos al coordinar componentes interconectados para asegurar la **confidencialidad, integridad y disponibilidad** de la información, usando técnicas como la encriptación, autenticación, control de acceso y mecanismos de tolerancia a fallos.  

## **Aspectos clave de la seguridad**

- **Autenticación**: verifica la identidad de usuarios y dispositivos para asegurar que son quienes afirman ser.  
- **Control de acceso**: define y aplica los permisos para que usuarios y procesos accedan a datos y recursos específicos.  
- **Integridad de datos**: asegura que la información no sea modificada o corrompida sin autorización.  
- **Disponibilidad**: garantiza que los datos y recursos estén accesibles cuando se necesiten, incluso ante fallos.  

---

## **Encriptación**

- **Propósito**: convierte los datos legibles en un formato codificado que es ininteligible para quienes no tienen la clave de descifrado.  

**Beneficios**:  
- Protección contra robo: incluso si los datos caen en manos de atacantes no podrán leerlos.  
- Privacidad: limita el acceso a los datos, tanto para usuarios externos como personal interno no autorizado.  

---

## **Tipos de encriptado**

- **Encriptación en tránsito**: protege los datos mientras viajan por la red, como en el caso de protocolos SSL/TLS.  
- **Encriptación en reposo**: protege los datos almacenados en dispositivos de almacenamiento como discos duros y/o bases de datos.  

---

## **Riesgos y amenazas**

Los ataques en los sistemas distribuidos dependen de la obtención de acceso a los canales de comunicación. Los métodos de ataque pueden clasificarse en función del modo en que se abusa del canal.  

### **1) Fisgar (Ransomware)**

Se refiere a la interceptación y copia no autorizada de mensajes que se transmiten entre nodos de una red. Es una forma de ataque que busca obtener información sensible o datos de comunicación sin permiso, violando la privacidad y seguridad del sistema.  

**Características**:  
- **Intercepción**: el atacante obtiene una copia de los mensajes que viajan a través de la red, que puede ser pública o privada.  
- **Sin autorización**: la acción se realiza sin el consentimiento de los propietarios del sistema o de los usuarios cuyas comunicaciones están siendo espiadas.  

---

### **2) Reenviar (Envenenamiento de caché DNS)**

- Es una forma de piratería informática en la que se introducen datos corruptos al sistema de nombres de dominio (DNS) en la caché del servidor, provocando que el servidor devuelva un registro incorrecto.  
- El atacante aprovecha vulnerabilidades del software DNS para redirigir a los usuarios de un sitio web a otro elegido por él.  

---

### **3) Suplantar (Phishing)**

- Es un tipo de ciberataque que utiliza correos electrónicos, mensajes de texto y/o llamadas para engañar a las personas y hacer que revelen información confidencial.  
- El objetivo principal del phishing es **robar dinero** o credenciales sensibles.  

---

# **Encriptación: roles principales**

La encriptación es el proceso de codificación de un mensaje de forma que queden ocultos sus contenidos. Cumple tres papeles principales:  

- **Secreto e integridad**  
- **Autenticación**  
- **Firmas digitales**  
