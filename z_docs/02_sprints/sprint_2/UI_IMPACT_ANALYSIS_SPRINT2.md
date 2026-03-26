# Entregable Día 1: Análisis de Impacto UI y Matriz de Contrato (Sprint 2)

**Responsable:** Luis (Frontend)
**Fecha:** 26 de Marzo de 2026
**Objetivo:** Mapear el impacto de los nuevos modelos (`Contact`, `ProjectContact`, `Document`) y campos (`planned/actual`, `work_notes`) en las vistas existentes de React y levantar alertas tempranas.

---

## 1. Matriz de Impacto (Pantalla -> Endpoint -> Campo -> Estado)

| Pantalla Afectada | Endpoint Relacionado | Campo(s) Nuevo(s) / Modificado(s) | Estado Actual |
| :--- | :--- | :--- | :--- |
| **Detalle de Proyecto** (`ProjectDetail.jsx`) | `GET /api/projects/{id}/` | `contacts` (Array de `ProjectContact` incl. `name`, `role`, `email`). | 🟢 Mocks UI creados. Esperando API. |
| **Detalle de Proyecto** (Sección Fases) | `GET /api/phases/?project={id}` | `planned_start_date`, `actual_start_date`, `planned_end_date`, `actual_end_date`. | 🟢 Mocks UI creados. Esperando API. |
| **Detalle de Proyecto** (Sección Fases/Tareas) | `GET /api/phases/?project={id}` | `notes_count`, `documents_count` (Agregados para evitar sobrecarga de carga inicial). | 🟢 Mocks UI creados. Esperando API. |
| **Modal / Vista de Contactos** (Nueva) | `POST /api/contacts/` y `POST /api/project-contacts/` | `name`, `email`, `phone`, `project_id`, `role`. | 🟡 Pendiente de definir estructura exacta con 3pleJ. |
| **Modal / Panel de Documentos** (Nueva) | `GET /api/documents/?phase={id}` | Lista de archivos vinculados a la fase/proyecto. | 🟡 En diseño. Bloqueado hasta estabilizar el modelo `Document`. |
| **Modal de Notas de Trabajo** (Nueva) | `GET /api/tasks/{id}/work_notes/` | Historial de `work_notes` por tarea. | 🟡 En diseño. |

---

## 2. Lista de Riesgos de UI por cambios de Backend

1. **Rendimiento por Payload Masivo (N+1):** * *Riesgo:* Si el backend decide anidar todos los textos de `work_notes` y los `Documents` dentro del GET general de Fases o Proyectos, el renderizado de React será muy lento.
   * *Mitigación:* Se solicita enviar únicamente **contadores** (`notes_count`, `documents_count`) en la carga inicial y usar endpoints separados para cargar el detalle cuando el usuario haga clic.
2. **Caída de UI por valores de fecha nulos:** * *Riesgo:* JS arrojará "Invalid Date" y crasheará la pantalla si `actual_start_date` o `actual_end_date` vienen con formatos inesperados o si el frontend asume que siempre traen datos.
   * *Mitigación:* Se implementará fallback en React para pintar estados como "Pendiente" si la fecha es nula, pero el backend debe asegurar el formato estricto `YYYY-MM-DD`.
3. **Desbordamiento Visual (Overflow) de Contactos:** * *Riesgo:* Si el proyecto tiene más de 10 contactos asociados mediante `ProjectContact`, la cabecera del proyecto se romperá visualmente.
   * *Mitigación:* El diseño actual en `ProjectDetail.jsx` usa un CSS Grid adaptable, pero se requerirá paginación del lado del backend si la lista escala.
4. **Validación Inconsistente de Roles:**
   * *Riesgo:* Si los roles en `ProjectContact` (ej. "Líder", "Auditor") se mandan como texto libre en lugar de un `Enum` o `ChoiceField` estricto, será imposible filtrar colores o iconos consistentes en la UI.
   * *Mitigación:* Cerrar la lista de opciones válidas para el campo `role` de Contact.

---
**Siguiente paso (Día 2):** Definir el archivo `frontend_payload_contract.md` con los ejemplos JSON reales para operaciones POST/PATCH y casos de error (400).