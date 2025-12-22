# Evaluación en Contacto con el Docente

![License](https://img.shields.io/badge/license-MIT-green)

## Estructura del Repositorio

Este repositorio está organizado en tres partes principales, cada una representando una fase clave del proyecto con su respectivo READMe.

### [PARTE 1: Evolución del Framework de Pruebas (Valor: 09 puntos)](./PARTE_1/PARTE_1.md)

En esta sección se aborda la creación y extensión de frameworks de pruebas, junto con la implementación de métricas avanzadas para evaluar la calidad del software.

*   **Sección 1: Comparación Práctica entre Frameworks (3 puntos)**
    *   Desarrollo de un mini-framework híbrido que combina características de Jasmine con funcionalidades avanzadas como pruebas de integración automática, mocking avanzado con espías personalizados y generación automática de pruebas basada en tipos.

*   **Sección 2: Extensión del Algoritmo de Búsqueda Binaria (3 puntos)**
    *   Ampliación del conjunto de pruebas para una implementación del algoritmo de búsqueda binaria, incorporando técnicas como *Property-based testing*, *Mutation testing* y *Contract testing*.

*   **Sección 3: Métricas Avanzadas de Calidad (3 puntos)**
    *   Implementación de un sistema de métricas que incluye complejidad ciclomática por prueba, detección de pruebas inestables (*flaky tests*), análisis de tiempo de ejecución y la relación entre cobertura y defectos detectados.

### [PARTE 2: Integración de Técnicas Avanzadas (Valor: 10 puntos)](./PARTE_2/PARTE_2.md)

Esta parte se enfoca en la automatización y orquestación de estrategias de prueba complejas dentro de un pipeline de integración continua.

*   **Sección 1: Orquestación de Pruebas Combinatorias (5 puntos)**
    *   Desarrollo de un sistema para generar casos de prueba combinatorios automáticamente, priorizarlos según el nivel de riesgo y optimizarlos utilizando modelos de predicción basados en ejecuciones previas.

*   **Sección 2: Pipeline de Testing Integral (5 puntos)**
    *   Diseño e implementación de un pipeline de testing que integra análisis estático (SonarQube), pruebas unitarias, de mutación y de cobertura (Istanbul, Jasmine, Stryker), pruebas combinatorias (ACTS), automatización sin código (TestCraft) y un modelo predictivo de confiabilidad (SMERFS, Frestimate).

### [PARTE 3: Investigación y Propuesta Innovadora (Valor: 09 puntos)](./PARTE_3/README.md)

La sección final consiste en una investigación comparativa y el diseño de una solución innovadora para la predicción de la confiabilidad del software.

*   **Sección 1: Comparación Codeless vs. Traditional (4 puntos)**
    *   Estudio comparativo entre herramientas de testing *codeless* (TestCraft), tradicionales (implementación propia con Jasmine) e híbridas (Selenium WebDriver).
    *   La evaluación se basa en métricas como tiempo de desarrollo, mantenibilidad, detección de defectos y ROI a 6 meses, incluyendo un análisis estadístico riguroso (pruebas de hipótesis, varianza y correlación).

*   **Sección 2: Modelo Predictivo Personalizado (5 puntos)**
    *   Diseño de un modelo de predicción de confiabilidad personalizado que utiliza datos históricos, métricas de complejidad y patrones de uso.
    *   El modelo combina enfoques logarítmicos y estocásticos para producir predicciones integradas por módulo.
