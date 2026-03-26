Asunto: Propuesta de proyecto de paralelización aplicada: Plataforma VIT (SGSI ISO 27001)

Estimado Profesor,

Espero que se encuentre muy bien.

Le escribo para presentarle mi propuesta de proyecto enfocada en la paralelización aplicada a un entorno real de backend. Actualmente estoy desarrollando la **Plataforma VIT**, un sistema backend en Django REST Framework y PostgreSQL diseñado para gestionar la implementación de la norma ISO 27001.

Mi propuesta central es **no paralelizar las operaciones CRUD transaccionales estándar, sino enfocar la paralelización en las tareas computacionalmente pesadas y naturalmente desacoplables del dominio del problema**. 

Específicamente, propongo aplicar paralelismo a los siguientes procesos críticos:
1. Generación masiva de reportes y documentos PDF.
2. Cálculo intensivo de matrices de riesgo (score inherente y residual).
3. Construcción del Statement of Applicability (SoA) basado en controles ISO.
4. Exportación del registro de auditoría y trazabilidad del sistema.

Para demostrar la viabilidad y el impacto de esta arquitectura, estructuraré el trabajo en 3 entregables principales:
1. **Diseño de la arquitectura paralela:** Estrategia de workers y colas de tareas asíncronas.
2. **Implementación de un piloto funcional:** Aplicado a la generación de reportes y/o recálculo de riesgos.
3. **Análisis experimental:** Comparación detallada entre la ejecución secuencial vs. paralela, documentando métricas de *speedup*, eficiencia e impacto en la latencia de la API principal.

Considero que este enfoque justifica el uso de computación paralela en un sistema de software aplicable a la industria real y permite derivar métricas claras y defendibles.

Quedo atento a sus comentarios o si prefiere que lo revisemos de forma presencial para afinar detalles.

Saludos cordiales,

[Tu Nombre/Firma]