# Entregable Día 2: Contrato de Payloads (Frontend -> API)

**Responsable:** Luis (Frontend)
**Fecha:** 26 de Marzo de 2026
**Objetivo:** Estandarizar la estructura de los requests (`POST`, `PATCH`), la transformación de datos en el frontend y la captura de errores (`400 Bad Request`) para los nuevos modelos del Sprint 2.

---

## 1. Transformación de Datos en Frontend

Antes de enviar cualquier payload al backend, el frontend aplicará las siguientes reglas de parseo:

* **Fechas:** Todas las fechas provenientes de inputs o datepickers se transformarán estrictamente al formato ISO 8601 corto: `YYYY-MM-DD`.
* **Valores Nulos:** Si un campo opcional (como `actual_end_date`) se limpia en el formulario, el frontend enviará explícitamente `null` (no un string vacío `""` ni `undefined`).
* **Enums Esperados (Ejemplos a validar con Backend):**
    * `ProjectContact.role`: `["LEAD", "AUDITOR", "STAKEHOLDER", "SPONSOR"]`
    * `Phase.type`: `["ASSESSMENT", "PLANNING", "IMPLEMENTATION", "AUDIT", "CERTIFICATION"]`
    * `Task.status`: `["PENDING", "IN_PROGRESS", "COMPLETED"]`

---

## 2. Payloads por Operación

### A. Contact & ProjectContact
*Como el backend está separando el Contacto de su asociación al proyecto, definimos los envíos así:*

**POST `/api/contacts/` (Crear nuevo contacto global)**
```json
{
  "name": "Ana Martínez",
  "email": "ana@empresa.com",
  "phone": "+573001234567"
}