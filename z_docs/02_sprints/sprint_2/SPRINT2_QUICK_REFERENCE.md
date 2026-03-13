# Sprint 2 - Quick Reference (BD-First)

Periodo: 11-24 marzo 2026
Objetivo: Cerrar y validar el modelo de base de datos antes de abrir API y frontend.

## Regla Operativa del Sprint

Hasta no cerrar BD, no se toca API ni frontend salvo fixes criticos.

No se crean serializers, viewsets, endpoints ni pantallas nuevas durante Fase 1-3.

## Estado Real al Iniciar

- Sprint 1: Completado.
- Assets: Integrado en backend y migrado.
- Pendiente: Contact, ProjectContact, Document, fechas planned/actual en Project-Phase-Task, migracion legacy de contactos.

## Alcance Congelado de Modelo

- Company
- Contact
- Project
- ProjectUser
- ProjectContact
- Phase
- Task
- Document
- Asset (sin rediseño en esta iteracion)

## Cambios de Esquema Obligatorios

- Company deja de ser dueno de contact_person y contact_position.
- Project, Phase y Task incorporan planned_start_date, planned_end_date, actual_start_date, actual_end_date.
- Task incorpora work_notes.
- Document entra como entidad formal de trazabilidad.

## Plan del Sprint (10 dias)

### Fase 1 - Congelar modelo (Dias 1-2)

- Cerrar diagrama final de datos.
- Cerrar nombres de campos, enums y relaciones.
- Aprobar constraints de integridad.

### Fase 2 - Persistencia solo BD (Dias 3-5)

- Implementar modelos y relaciones.
- Crear migraciones estructurales.
- Crear data migration legacy Company -> Contact.

### Fase 3 - Validacion de integridad (Dias 6-8)

- Validar constraints y reglas de consistencia.
- Probar creacion/relaciones en shell y tests basicos.
- Corregir issues de migracion.

### Fase 4 - Abrir API (Dias 9-10)

- Solo cuando la BD este cerrada.
- Habilitar serializers y viewsets por prioridad.

## Comandos Clave

```bash
cd backend

# 1) Crear migraciones del cambio de modelo
python manage.py makemigrations

# 2) Aplicar migraciones
python manage.py migrate

# 3) Validar proyecto
python manage.py check

# 4) Inspeccion de modelo
python manage.py shell

# 5) Ver estado de migraciones
python manage.py showmigrations
```

## Checklist de Cierre de BD

- [ ] Diagrama final aprobado.
- [ ] Models definitivos aprobados.
- [ ] Migraciones limpias en entorno local.
- [ ] Data migration legacy validada.
- [ ] Constraints probados.
- [ ] Sin cambios pendientes en nombres, relaciones ni enums.

## Criterio de Hecho del Sprint 2

Sprint 2 se considera exitoso si la BD queda estable y aprobada, incluso si API y frontend quedan para la siguiente iteracion.

Esto minimiza retrabajo y evita romper contratos de datos.
