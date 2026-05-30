# Manual de Usuario - Préstamos NNY

## Descripción
Préstamos NNY es una aplicación de consola para gestionar préstamos de objetos entre amigos. Permite registrar amigos, prestar artículos, registrar devoluciones y consultar información administrativa.

---

## Requisitos

- Python 3.x
- Archivos CSV:
  - `clientes.csv`
  - `objetos.csv`
  - `usuarios.csv`

---

## Inicio del programa

Ejecute el archivo principal:

```bash
python app.py
```

Al iniciar, el sistema cargará automáticamente la información almacenada en los archivos CSV.

---

## Menú Principal

### 1. Registrar Amigo
Permite registrar un nuevo amigo en el sistema.

Datos solicitados:
- Nombre
- Apellido
- Documento
- Correo electrónico
- Tipo de préstamo

### 2. Registrar Préstamo
Permite asignar un objeto a un amigo registrado.

Proceso:
1. Seleccionar amigo.
2. Seleccionar objeto disponible.
3. Definir el tiempo de préstamo.
4. Confirmar el registro.


### 3. Registrar Devolución
Permite registrar la devolución de un objeto prestado.

El sistema actualizará automáticamente el estado del artículo.

### 4. Consultar Items con más de 30 días
Muestra los préstamos que han superado el tiempo establecido.

### 5. Consultar Artículos Prestados
Lista los artículos actualmente prestados.

### 6. Administrador
Acceso a funciones administrativas mediante usuario y contraseña.

---

## Módulo Administrador

Para ingresar:

1. Seleccione la opción **Administrador**.
2. Ingrese usuario y contraseña.
3. Si las credenciales existen en `usuarios.csv`, se habilitará el panel administrativo.



### Opciones disponibles

#### 1. Total de Préstamos Registrados
Muestra todos los préstamos almacenados.

#### 2. Total de Items Devueltos
Presenta la cantidad total de devoluciones realizadas.

#### 3. Total de Ventas Realizadas
Muestra los artículos vendidos.

#### 4. Total de Pagos Realizados
Consulta los pagos registrados.

#### 5. Lista de Amigos
Muestra todos los amigos registrados.

#### 6. Amigos con Mayor y Menor Cantidad de Préstamos
Genera estadísticas de uso por usuario.

---

## Validaciones

### Nombres y Apellidos
- Mínimo 3 caracteres.
- Solo letras.
- No se permiten espacios.

### Documento
- Entre 3 y 15 dígitos.
- Solo números.

### Correo Electrónico
- Debe contener un único símbolo `@`.
- Debe finalizar en `.com`.
- No puede contener espacios.

### Valores Numéricos
- Solo números positivos.

---

## Estados de los Objetos

| Estado | Descripción |
|----------|-------------|
| 0 | Disponible |
| 1 | Prestado |
| 2 | Vendido |

---


## Categorías de Objetos

- Videojuegos
- Libros
- Música y video
- Herramientas
- Dinero
- Misceláneo y varios

---

## Almacenamiento de Datos

La información se guarda en archivos CSV:

### clientes.csv
Información de los amigos registrados.

### objetos.csv
Inventario y estado de los objetos.

### usuarios.csv
Credenciales de acceso al módulo administrativo.

---


## Solución de Problemas

### No puedo iniciar sesión
Verifique:
- Usuario correcto.
- Contraseña correcta.
- Existencia del archivo `usuarios.csv`.

### No aparecen registros
Verifique que los archivos CSV existan y tengan datos válidos.

### Error al importar datos
Revise el formato de los archivos CSV y los permisos de lectura.

---

## Autor

Sistema desarrollado como proyecto académico para la gestión de préstamos de objetos entre amigos.


