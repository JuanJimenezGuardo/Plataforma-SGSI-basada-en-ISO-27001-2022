# Propuesta de Paralelización de Procesos Críticos en la Plataforma VIT (SGSI ISO 27001)

## 1. Resumen Ejecutivo
El presente documento propone el diseño e implementación de una arquitectura paralela para procesos pesados dentro de la plataforma **VIT**, un backend transaccional (Django REST + PostgreSQL) enfocado en la gestión de Sistemas de Gestión de Seguridad de la Información (ISO 27001). El objetivo es demostrar los beneficios del paralelismo a nivel de tareas en un entorno real, midiendo el *speedup* y la mejora en el rendimiento sin comprometer la consistencia de las operaciones CRUD del negocio.

## 2. Descripción del Problema
Si bien la arquitectura monolítica secuencial de VIT maneja eficientemente las peticiones HTTP transaccionales estándar, el sistema contempla procesos que crecen lineal o exponencialmente en costo computacional conforme aumenta la cantidad de usuarios, proyectos y activos de información. Estos cuellos de botella incluyen:
* Generación de reportes PDF detallados (documentos de cumplimiento).
* Recálculos masivos de matrices de riesgo (impacto vs probabilidad).
* Ensamblaje del Statement of Applicability (SoA) cruzando múltiples controles ISO.
* Exportación y procesamiento de logs de auditoría masivos.

La ejecución síncrona de estas tareas bloquea el hilo principal, degradando la experiencia del usuario y limitando el *throughput* del sistema.

## 3. Estrategia de Paralelización
La estrategia radicará en un patrón de concurrencia basado en el despachador de tareas (Task Queues / Workers). No se paralelizarán peticiones HTTP directas ni operaciones de alta consistencia transaccional. En su lugar, el modelo aplicará el paradigma **Task-Level Parallelism** para:

1. **Aislamiento Computacional:** Separar las cargas pesadas (CPU y I/O Bound) del flujo principal del servidor web.
2. **Procesamiento Concurrente:** Levantar múltiples *workers* que procesen colas de trabajos simultáneamente (ej. calcular el riesgo de 50 servidores al mismo tiempo).
3. **Desacoplamiento del Dominio:** Asegurar de que cada tarea paralela es independiente y libre de *race conditions* en la capa de datos.

## 4. Metodología y Plan de Trabajo
La implementación se validará mediante un flujo de trabajo de 3 fases:

1. **Fase de Diseño:** Modelado de la separación síncrono/asíncrono, diseño de endpoints para disparar *jobs* y consultar estados (Polling/WebSockets), e instanciación del *broker* de mensajería.
2. **Fase de Implementación Piloto:** Desarrollo del mecanismo de procesamiento en background focalizado en uno o dos casos de uso críticos (Ej: Recálculo de riesgos y Generación de Reportes).
3. **Fase de Experimentación y Medición:** Pruebas de carga utilizando *data sets* sintéticos que simulan corporaciones de diferente tamaño, registrando tiempos bajo un esquema secuencial estricto vs. un esquema concurrente con *N* workers físicos/lógicos.

## 5. Métricas de Evaluación Esperadas
Se presentarán los resultados en base a las siguientes métricas de ciencias de la computación aplicadas:
* **Tiempo Secuencial ($T_{seq}$)** vs **Tiempo Paralelo ($T_{par}$)** de los *jobs* medidos.
* **Speedup ($S$)**: Evaluación de la mejora relativa obtenida.
* **Eficiencia ($E$)**: Ratio del *speedup* entre la cantidad de hilos/workers dedicados.
* **Mejora en la Latencia de la API**: Reducción del tiempo de respuesta del endpoint HTTP que coordina la petición.

## 6. Justificación Académica
El proyecto plantea un escenario de paralelización de la vida real, alejándose de los ejemplos puramente teóricos. Permite analizar el compromiso (*trade-off*) entre el *overhead* de la gestión de colas/concurrencia y el beneficio obtenido al descargar la API principal, aplicando los fundamentos de concurrencia y paralelismo sobre infraestructura moderna de backend.