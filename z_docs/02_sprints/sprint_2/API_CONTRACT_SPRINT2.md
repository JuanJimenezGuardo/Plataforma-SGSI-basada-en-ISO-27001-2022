# Contrato de API - Actualizaciones Sprint 2

**Fecha:** 26 de Marzo de 2026
**Responsables:** Luis (Frontend) / Oscar y Juan Jose (Backend)
**Objetivo:** Definir la estructura de datos requerida por la nueva UI del Sprint 2 para soportar la visualización de Contactos asignados, control de Fechas (Planned/Actual) y contadores de Notas/Documentos.

---

## 1. Módulo de Proyectos (Project Details)
**Endpoint:** `GET /api/projects/{id}/`

### Cambios Requeridos
Se requiere incluir una nueva propiedad `contacts` que devuelva un array con la información de las personas de contacto asignadas al proyecto a través del nuevo modelo `ProjectContact`.

### Payload Esperado (Ejemplo de Respuesta)
```json
{
  "id": 1,
  "name": "Implementación ISO 27001 - ACME",
  "description": "Proyecto de implementación completa de SGSI...",
  "company": 1,
  "company_name": "ACME Corporation",
  "status": "IN_PROGRESS",
  "start_date": "2026-02-25",
  "end_date": "2026-07-25",
  "created_by": 2,
  "created_by_name": "Ana Martínez",
  
  // ---> NUEVA SECCIÓN REQUERIDA <---
  "contacts": [
    {
      "id": 1,                  // ID de la relación ProjectContact
      "contact_id": 15,         // ID del modelo Contact
      "name": "Ana Martínez",
      "role": "Líder de Proyecto",
      "email": "ana@empresa.com"
    },
    {
      "id": 2,
      "contact_id": 22,
      "name": "Carlos Ruiz",
      "role": "Auditor Externo",
      "email": "cruiz@vit.com"
    }
  ]
}