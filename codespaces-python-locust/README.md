# Proyecto de Fibonacci y Locust

Este proyecto contiene un script de Python que implementa la secuencia de Fibonacci y utiliza Locust para realizar pruebas de carga.

## Estructura del Proyecto

```
codespaces-python-locust
├── .devcontainer
│   ├── devcontainer.json       # Configuración del contenedor de desarrollo
│   └── Dockerfile              # Definición de la imagen del contenedor
├── src
│   └── fibonacci.py            # Script de Python para la secuencia de Fibonacci
├── locust
│   └── locustfile.py           # Script de configuración para Locust
├── requirements.txt            # Dependencias del proyecto
├── start.sh                    # Script de inicio para ejecutar Fibonacci y Locust
├── .gitignore                  # Archivos y directorios a ignorar por Git
└── README.md                   # Documentación del proyecto
```

## Requisitos

Asegúrate de tener las siguientes herramientas instaladas:

- Docker
- Git

## Configuración del Entorno

1. Clona el repositorio:
   ```bash
   git clone <url-del-repositorio>
   cd codespaces-python-locust
   ```

2. Abre el proyecto en GitHub Codespaces.

3. El entorno se configurará automáticamente utilizando el archivo `.devcontainer`.

## Ejecución del Script de Fibonacci

Para ejecutar el script de Fibonacci, utiliza el siguiente comando:

```bash
python src/fibonacci.py
```

## Ejecución de Locust

Para iniciar las pruebas de carga con Locust, ejecuta:

```bash
locust -f locust/locustfile.py
```

Luego, abre tu navegador y ve a `http://localhost:8089` para acceder a la interfaz de usuario de Locust.

## Iniciar Todo

Puedes ejecutar el script de Fibonacci y luego iniciar Locust utilizando el script de inicio:

```bash
bash start.sh
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.