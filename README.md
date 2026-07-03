# Manual de Configuración del Repositorio (Flask + MySQL + Docker)

Este repositorio contiene una aplicación web básica construida con Flask que se conecta a una base de datos MySQL, todo orquestado mediante Docker Compose.

## Requisitos Previos

- [Docker](https://www.docker.com/get-started) instalado.
- [Docker Compose](https://docs.docker.com/compose/install/) instalado.

## Estructura del Proyecto

- `app.py`: Aplicación principal en Flask.
- `Dockerfile`: Instrucciones para construir la imagen de la aplicación Flask.
- `docker-compose.yml`: Configuración de los servicios (app y db).
- `empresa.sql`: Script SQL para inicializar la base de datos y tablas.
- `requirements.txt`: Dependencias de Python.

---

## Pasos para Crear y Ejecutar el Entorno

### 1. Construir e Iniciar los Contenedores

Para construir las imágenes y levantar los contenedores por primera vez, ejecuta:

```bash
docker-compose up --build
```

*(Agrega aquí una imagen del proceso de construcción)*
![Proceso de Build](ruta/a/tu/imagen_build.png)

### 2. Verificar los Contenedores en Ejecución

Puedes verificar que ambos contenedores (`flask_app` y `mysql_db`) están corriendo con:

```bash
docker ps
```

### 3. Acceder a la Aplicación

Una vez que los contenedores estén listos, abre tu navegador y ve a:

[http://localhost:8081](http://localhost:8081)

Aquí verás la interfaz de la aplicación con los datos cargados desde la base de datos.

*(Agrega aquí una imagen de la aplicación funcionando)*
![App Funcionando](ruta/a/tu/imagen_app.png)

---

## Comandos Útiles de Docker

### Detener los Contenedores
```bash
docker-compose stop
```

### Eliminar los Contenedores y Redes
```bash
docker-compose down
```

### Ver Logs de la Aplicación
```bash
docker-compose logs -f app
```

### Acceder a la Base de Datos MySQL (desde terminal)
```bash
docker exec -it mysql_db mysql -u root -p123456 empresa
```

---

## Mejora del Estilo y Datos

La página ha sido mejorada con un diseño moderno usando CSS embebido en `app.py`. Los datos mostrados se inicializan automáticamente mediante el archivo `empresa.sql` al levantar el servicio de base de datos por primera vez.

*(Agrega aquí una imagen del diseño mejorado)*
![Diseño Mejorado](ruta/a/tu/imagen_estilo.png)
