#!/bin/bash

# Ejecutar el script de Fibonacci
python3 src/fibonacci.py

# Iniciar Locust
locust -f locust/locustfile.py --host=http://localhost:8000