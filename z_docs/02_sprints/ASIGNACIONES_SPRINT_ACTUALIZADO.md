# Asignaciones por Sprint (Sprint 1-6)

ESTRUCTURA DEL PROYECTO:
- Sprint 1 (COMPLETADO): 3pleJ ha ejecutado TODO (100%)
- Sprints 2-6: En ejecucion por fases con prioridad de base de datos

IMPORTANTE: Todos los sprints estan condicionados por la arquitectura de produccion definida en ARQUITECTURA_DESPLIEGUE_PRODUCCION.md.

---

## SPRINT 1 (19 feb -> 2 mar) - Seguridad Base + Auth [COMPLETADO]

Objetivo: Pasar de API abierta a plataforma con control de acceso real.

Estado: Completado.

---

## SPRINT 2 (11 mar -> 24 mar) - Reorganizado BD-First [EN CURSO]

Objetivo del sprint:
Cerrar modelo de base de datos para alinearlo con requerimientos del ingeniero y mockups.

Regla del sprint:
Hasta no cerrar BD, no se desarrollan API ni frontend nuevos salvo fixes criticos.

### Alcance congelado de entidades

- Company
- Contact
- Project
- ProjectUser
- ProjectContact
- Phase
- Task
- Document
- Asset (sin rediseño)

### Asignaciones por rol

#### 3pleJ (Arquitectura y coordinacion)

- [ ] Aprobar diagrama final de datos
- [ ] Congelar nombres de campos y enums
- [ ] Definir reglas de integridad
- [ ] Aprobar criterio de BD cerrada

#### Osky (Backend persistencia)

- [ ] Implementar Contact y ProjectContact
- [ ] Implementar Document
- [ ] Agregar fechas planned/actual en Project, Phase y Task
- [ ] Agregar work_notes en Task
- [ ] Crear migraciones y data migration legacy
- [ ] Validar constraints

#### Tinky (Frontend)

- [ ] Congelar nuevas pantallas durante Fase 1-3
- [ ] Corregir solo bugs criticos
- [ ] Preparar mapa de pantallas para contrato de datos final
- [ ] Iniciar integracion solo cuando BD este aprobada

### Plan semanal

Semana 1:
- [ ] Diseno final del modelo
- [ ] Implementacion de modelos
- [ ] Migraciones estructurales

Semana 2:
- [ ] Data migration legacy
- [ ] Validacion de integridad
- [ ] Apertura de API minima al final del sprint (si BD cerrada)

### Criterio de cierre de Sprint 2

- [ ] Diagrama final aprobado
- [ ] Models definitivos aprobados
- [ ] Migraciones limpias
- [ ] Data migration legacy validada
- [ ] Constraints probados
- [ ] API habilitada solo despues de estabilidad de esquema

---

## SPRINT 3 (Propuesto) - Riesgos

Inicia solo si Sprint 2 cierra BD estable.

---

## SPRINT 4 (Propuesto) - SoA + ISO Controls

Dependiente de cierre de Sprint 3.

---

## SPRINT 5 (Propuesto) - Evidence + Audit

Dependiente de cierre de Sprint 4.

---

## SPRINT 6 (Propuesto) - Reports + Dashboard

Dependiente de cierre de Sprint 5.
