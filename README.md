# Markdown
# 1. Prestamos - NNY
#### ACTAS
#### ACTA DE ENTENDIMIENTO

Reunión el día 23 de marzo de 2026 a las 3 pm
Discutimos la elaboración del trabajo y hablamos de los temas que entendimos, concluimos que estamos un poco confundidos porque no sabemos cómo empezar.

Expectativas:
Realizar el trabajo de manera correcta
Aprender de python y sus comandos adecuadamente
Entender cómo este tipo de actividades nos ayudan a ser más eficientes en nuestros empleos actuales y en los futuros como ingenieros.

Reunión 25 de marzo 2026 a las 7 pm
se hacen avances hasta el punto 4, y se deja pendiente consultar sobre el punto 5.

Reunión 27 de marzo 2026 a las 8 pm
se hace avance del punto 5 y se acuerda que el punto 6 lo realiza Nelson y el punto 7 Nathalia y Yovana
#### ACTA DE COLABORACIÓN
23 marzo de 2026 a las 3 pm

Encuentro
Saludo
avance en el trabajo e ideas
elaboración de las ideas y pendientes

Canales de comunicación
Whatsapp

Horarios de encuentros 
Miércoles - Viernes  7pm a 10 pm (depende de la actividad)

Sanciones
Se expulsará del grupo a quien no participe ni se pronuncie por ningún medio de comunión sobre el trabajo.
Excluir de las actas al integrante que no se conecte en los horarios establecidos, siempre y cuando no haya presentado una excusa válida.
#### ACTA DE RESPONSABILIDAD
23 de marzo de 2026 a las 3 pm

Aún no se delegan actividades, ya que tenemos dudas de como empezar el taller, quedamos que el día de mañana en clases vamos aclarar las dudas y a partir de allí delegamos los puntos correspondientes de a cada integrante.

Dudas para la clase del martes 24 de marzo de 2026
- ¿Cómo empezamos el trabajo?
- las acta al momento de la entrega van en normas APA 
- ¿Cómo realizar el repositorio?

Reunión 27 de marzo 2026 a las 8 pm
se acuerda que el punto 6 lo realiza Nelson y el punto 7 Nathalia y Yovana

# 2. Integrantes
- Nathalia Buelvas Diaz
**Habilidades:** trabajo en artes manuales, tengo una buena capacidad de oralidad. 
- Nelson Garcia Montoya
**Habilidades:** Comunicacion en equipo, Pensamiento analítico y optimización
- Yovana Patricia López Marin
**Habilidades:** trabajo en equipo, analisis y comunicación verbal.
## **programa:** Ingenieria Industrial
# 3. Prestamos-NNY
#### Es un proyecto orientado a la ayuda en la gestion del sistema de prestamos elaborado en Python, donde se pueda tener control, seguimiento y devoluciones de los recursos, teniendo un control de sanciones y seguimiento en tiempo real de los prestamos.
el nombre *Prestamos-NNY* nacio de la necesidad crear un nombre con sentido propio
## 4. Licencia del Sotfware [http://www.apache.org/licenses/](https://url.com)

Nota:la licencia ya esta adjuntada en el archivo.
## 5. Reporte de visión 
Michael Jackson Gamboa nos solicita realizar un programa donde no se le olvide a quien le presta sus juegos, herramientas, electrodomésticos y múltiples cosas a sus amigos, pues dado que tiene tantas cosas algunas veces se le pierden por la falta de control, por lo cual nos solicita crear un inventario de sus pertenecias y un listados de sus amigos con sus datos basicos, como nombre, cedula, correo y telefono celular. Adicional el manifiesta que tiene un tiempo de prestamos, lo ideal es que despues de 20 días el programa genere un recordatorio y genere notificaciones y genere documentos de devolución, pasados 30 días el programa debe generar facturarción del elemento prestado por el valor de adquisición inicial, esto esta previamente acordado al inicio de la entrega.
La finalidad de dicho programa es tener control en tiempo real de los elementos prestados y evitar que Michael pierda sus enseres.
## 6. Especificación de requisitos
**Requisitos Funcionales**
Los requisitos funcionales definen las acciones específicas y operaciones que el sistema debe ejecutar:

**Gestión de Usuarios:**  El sistema debe permitir el registro de usuarios validando que el nombre y apellido tengan una longitud mínima de tres letras y no contengan números.

-Debe validar que el documento de identidad tenga entre 3 y 15 dígitos numéricos sin letras u otros caracteres.

-Debe verificar que el correo electrónico contenga un "@" y termine en "." y "com".

-Debe permitir asignar un tiempo de préstamo fijo al crear el usuario, eligiendo únicamente entre 5, 10, 15 o 30 días.


**Gestión de Ítems (Inventario):** El sistema debe permitir registrar ítems con un nombre de al menos tres letras, permitiendo el uso de números.

-Debe categorizar el ítem exclusivamente en: Videojuegos, Libros, Música y video, Herramientas, Dinero, o Misceláneo y varios.

-Debe registrar el precio de compra del artículo.Debe generar un ID único alfanumérico asociado a la categoría del ítem.

-Debe registrar la calidad o estado del ítem utilizando lógica difusa.


**Gestión de Préstamos:** El sistema debe permitir registrar préstamos únicamente a usuarios previamente registrados en el sistema, buscando el ítem por su código o ID.

-Debe generar notificaciones de recuperación o solicitud de devolución cuando hayan pasado al menos 20 días desde el préstamo.


**Devoluciones y Certificados:** El sistema debe permitir registrar devoluciones validando que el usuario tenga préstamos activos

-Al realizar una devolución a tiempo, debe generar un certificado en un documento de texto plano (con opción a bono si es PDF), nombrado con el nombre del prestador, la fecha de devolución y el ID.


**Facturación por Retraso:** Si un ítem supera los 30 días de préstamo, el sistema debe generar una venta obligatoria al prestador.

-Debe generar una factura en archivo de texto plano (bono si es PDF) calculando el subtotal, el total, y aplicando un impuesto adicional por "conchudez" del 23%.


**Consultas y Reportes:** El sistema debe permitir consultar los ítems prestados ordenados por cantidad de días usando estadísticas generales.


**Módulo de Administrador:** El sistema debe restringir el acceso al módulo de administración mediante un usuario y contraseña válidos.

-El submódulo debe generar reportes sobre: total de préstamos registrados, total de ítems devueltos, total de ventas, total de pagos realizados, lista de usuarios, y usuarios con mayor y menor cantidad de préstamos.

**Requisitos No Funcionales**
Los requisitos no funcionales especifican los criterios para juzgar la operación del sistema, como rendimiento, usabilidad y compatibilidad:

**Interfaz de Usuario (Usabilidad):** El programa debe tener un menú amigable basado en la consola que permita navegar entre las opciones de registro, consultas y administración.

**Almacenamiento de Datos (Persistencia):** Toda la información de usuarios, préstamos y estadísticas debe gestionarse mediante archivos planos.

**Compatibilidad y Exportación:** El sistema debe ser capaz de exportar los resultados y la información gestionada a un archivo CSV utilizando Python.

**Estructura del Proyecto:** El código fuente completo debe estar alojado en una carpeta llamada "src" dentro del repositorio de GitHub.



## 7. Plan de proyecto 
*CRONOGRAMA*

<img width="706" height="230" alt="image" src="https://github.com/user-attachments/assets/6281a4d9-b047-40a1-acaa-d43e9feece1f" />

*PRESUPUESTO*

- Salario base 2026 $1.423.500
- Cantidad de horas mensuales 220 (jornada de 44 horas)
- Cantidad de horas requeridas para este trabajo 50 
<img width="897" height="128" alt="image" src="https://github.com/user-attachments/assets/c6930e5d-5700-47b5-938d-7ba28e8eb3d1" />



