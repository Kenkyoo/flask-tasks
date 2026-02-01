# Flask Tasks

## Descripción

Este proyecto es una aplicación web desarrollada con Flask que permite crear, editar y eliminar tareas. La aplicación utiliza una base de datos SQLite para almacenar las tareas.

## Requisitos

- Python 3.11 o superior
- Docker

## Instalación

1. Clona el repositorio:

```
git clone https://github.com/usuario/flask-tasks.git
```

2. Cambia al directorio del proyecto:

```
cd flask-tasks
```

3. Construye la imagen de Docker:

```
docker-compose build
```

4. Inicia el contenedor:

```
docker-compose up
```

5. Abre tu navegador en http://localhost:8000 para ver la aplicación.

## Uso

1. Ingresa a http://localhost:8000 en tu navegador.

2. Crea una nueva tarea escribiendo el título y la descripción en los campos correspondientes y presionando el botón "Crear".

3. Edita una tarea haciendo clic en el botón "Editar" y modificando los campos correspondientes.

4. Elimina una tarea haciendo clic en el botón "Eliminar".

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor crea un pull request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
