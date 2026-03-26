# Entregable Día 4: Checklist de Compatibilidad UI/API (Sprint 2)

**Responsable:** Luis (Frontend)
**Fecha:** 26 de Marzo de 2026
**Objetivo:** Validar que los endpoints actualizados por el backend no rompan la UI actual y que los nuevos campos se rendericen correctamente.

## 1. Lectura de Datos (`GET`)

| Flujo a probar | Endpoint | Resultado Esperado | Resultado Obtenido (Status Code) | Evidencia / Notas | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Detalle Proyecto** | `GET /api/projects/{id}/` | Retorna array `contacts` sin romper la vista principal. | `[   ]` | *(Insertar enlace a captura o log)* | ⬜ Pendiente |
| **Listado Fases** | `GET /api/phases/?project={id}` | Retorna `planned_start_date` y `notes_count`. Fechas se ordenan bien. | `[   ]` | *(Insertar enlace a captura o log)* | ⬜ Pendiente |

## 2. Creación y Edición (`POST` / `PATCH`)

| Flujo a probar | Endpoint | Payload Enviado | Resultado Obtenido (Status Code) | Evidencia / Notas | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Crear Contacto** | `POST /api/contacts/` | `{ "name": "Test", "email": "t@t.com"... }` | `[   ]` | *(Insertar captura de Red/Console)* | ⬜ Pendiente |
| **Vincular Contacto** | `POST /api/project-users/` | `{ "project": 1, "user": 2, "role": "CONSULTANT" }` | `[   ]` | *(Insertar captura de Red/Console)* | ⬜ Pendiente |
| **Actualizar Fechas** | `PATCH /api/phases/{id}/` | `{ "actual_start_date": "2026-03-26" }` | `[   ]` | *(Insertar captura de Red/Console)* | ⬜ Pendiente |

## 3. Manejo de Errores y Nulos

- [ ] UI no "crashea" si `actual_end_date` viene como `null`.
- [ ] UI muestra error 400 correctamente si se envía un email inválido al crear contacto.
- [ ] UI muestra error 403 si un rol `CLIENT` intenta asignar un contacto.