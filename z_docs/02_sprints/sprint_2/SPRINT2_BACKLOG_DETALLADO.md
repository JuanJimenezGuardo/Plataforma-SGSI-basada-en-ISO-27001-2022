# Sprint 2 - Backlog Detallado (BD-First)

Duracion: 2 semanas (11-24 marzo)
Objetivo: Cerrar el modelo de datos solicitado por ingenieria y dejar BD estable.

## Politica de Prioridad

Durante este sprint se trabaja primero persistencia. API y frontend se abren solo al final cuando la BD este cerrada.

## Alcance Tecnico Congelado

- Company
- Contact
- Project
- ProjectUser
- ProjectContact
- Phase
- Task
- Document
- Asset (sin rediseño)

## Backlog por Fases

### Fase 1 - Diseno final de BD (Dias 1-2)

1. Cerrar diagrama final con relaciones y cardinalidades.
2. Congelar enums y nombres de campos.
3. Definir constraints de integridad.

Entregables:
- Diagrama aprobado.
- Lista final de campos por entidad.
- Reglas de validacion aprobadas.

### Fase 2 - Implementacion de persistencia (Dias 3-5)

1. Crear modelo Contact.
2. Crear modelo ProjectContact con regla de consistencia de empresa.
3. Crear modelo Document con estados y aprobacion.
4. Agregar fechas planned/actual a Project, Phase y Task.
5. Agregar work_notes en Task.
6. Mantener Asset como esta.

Entregables:
- Modelos implementados.
- Constraints implementados.
- Migraciones estructurales creadas.

### Fase 3 - Migracion legacy y validacion (Dias 6-8)

1. Data migration de Company.contact_person/contact_position a Contact.
2. Validar constraints y relaciones.
3. Verificar integridad de fechas y consistencia project-phase-task-document.
4. Ajustes de migracion sin abrir API.

Entregables:
- Migracion legacy validada.
- BD consistente en entorno local.

### Fase 4 - Habilitacion API minima (Dias 9-10)

1. Abrir serializers basicos.
2. Abrir viewsets por prioridad: Contact, ProjectContact, Document.
3. Mantener frontend congelado hasta contrato de datos estable.

Entregables:
- Primer corte de API sobre esquema estable.

## Lista de Tareas Operativas

- [ ] Actualizar models de companies/projects/phases/tasks.
- [ ] Crear app contacts (o modulo en companies, segun decision final).
- [ ] Crear app documents (o modulo en projects, segun decision final).
- [ ] Crear y ejecutar migraciones.
- [ ] Ejecutar data migration legacy.
- [ ] Ejecutar validaciones tecnicas.

## Validaciones Obligatorias

```bash
cd backend
python manage.py makemigrations
python manage.py migrate
python manage.py check
python manage.py showmigrations
```

## Definicion de BD Cerrada

1. Diagrama final aprobado.
2. Models definitivos aprobados.
3. Migraciones limpias.
4. Data migration legacy validada.
5. Constraints probados.
6. Sin cambios pendientes en nombres, relaciones o enums.

## Riesgo que Evita este Plan

- Cambios de payload a mitad de desarrollo.
- Retrabajo de frontend por cambios de API.
- Rotura de migraciones por cambios tardios de esquema.
