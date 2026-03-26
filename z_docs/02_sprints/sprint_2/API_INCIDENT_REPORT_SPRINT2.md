# Entregable Día 5: Reporte de Incidencias de Contrato (Sprint 2)

**Responsable:** Luis (Frontend)
**Revisor:** Osky / 3pleJ (Backend)
**Fecha:** 26 de Marzo de 2026

A continuación, se detallan las desalineaciones encontradas entre el contrato acordado y el comportamiento actual de los endpoints en el entorno de desarrollo.

## 🔴 Severidad Alta (Bloqueantes funcionales)

**INCIDENCIA-01: El endpoint de creación de contactos arroja 500 en lugar de 400 al enviar email inválido.**
* **Endpoint:** `POST /api/contacts/`
* **Request Enviado:** `{ "name": "Luis", "email": "correo-malo" }`
* **Respuesta Obtenida:** `500 Internal Server Error` (Falla de base de datos / IntegrityError).
* **Respuesta Esperada:** `400 Bad Request` con el mensaje: `{"email": ["Introduzca una dirección de correo electrónico válida."]}`.
* **Impacto UI:** La UI no puede capturar el error para mostrarlo en el input rojo. El usuario ve un error genérico del servidor.

## 🟡 Severidad Media (Desalineación de Nomenclatura o Reglas)

**INCIDENCIA-02: ProjectContact acepta roles fuera del Enum definido.**
* **Endpoint:** `POST /api/project-contacts/`
* **Request Enviado:** `{ "project": 1, "contact": 1, "role": "HACKER" }`
* **Respuesta Obtenida:** `201 Created`
* **Respuesta Esperada:** `400 Bad Request` indicando que el rol no es una opción válida.
* **Impacto UI:** Si la BD acepta roles basura, los filtros de la UI y los iconos condicionales se romperán al leerlos.

## 🟢 Severidad Baja (Ajustes Menores)

**INCIDENCIA-03: Formato de respuesta de fechas incluye horas (DateTime) en lugar de Date.**
* **Endpoint:** `GET /api/phases/?project=1`
* **Respuesta Obtenida:** `"planned_start_date": "2026-03-01T10:00:00Z"`
* **Respuesta Esperada:** `"planned_start_date": "2026-03-01"`
* **Impacto UI:** Obliga al frontend a parsear el string extra antes de inyectarlo en los componentes visuales.