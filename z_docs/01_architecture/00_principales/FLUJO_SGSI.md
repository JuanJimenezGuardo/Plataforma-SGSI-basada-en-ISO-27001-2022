# Flujo del Sistema SGSI ISO 27001

Fecha: 2026-03-19
Responsable: Juan Jose Jimenez Guardo

## Objetivo

Documentar el flujo operativo de la plataforma VIT para implementar un SGSI ISO 27001, desde la creacion de una empresa hasta el registro de auditoria.

## Explicacion del modelo de datos

El modelo relacional esta disenado con enfoque multi-tenant, donde la entidad Empresa
define el perimetro de datos y cada proyecto SGSI queda ligado a una empresa especifica.

Entidades principales del flujo:

- Empresa: organizacion cliente sobre la que se ejecuta el SGSI.
- Proyecto: contenedor del ciclo de implementacion ISO 27001 por empresa.
- Contacto y ProyectoContacto: personas vinculadas al cliente y su asignacion al proyecto.
- Activo: recursos de informacion e infraestructura evaluados en el SGSI.
- Fase y Tarea: estructura operativa para planificar, ejecutar y controlar avance.
- Documento: evidencia formal, politicas y registros del sistema.
- RegistroAuditoria: trazabilidad de acciones y cambios sobre entidades criticas.

Relaciones clave:

- Empresa 1:N Proyecto.
- Empresa 1:N Contacto.
- Proyecto N:M Contacto (resuelto mediante ProyectoContacto).
- Proyecto 1:N Activo, Fase y Documento.
- Fase 1:N Tarea.
- Usuario 1:N RegistroAuditoria.

## Flujo basado en el modelo

Empresa -> Proyecto -> Contacto -> Activo -> Fase -> Tarea -> Documento -> Auditoria

## 1) Creacion de empresa

- Un administrador o consultor registra la empresa cliente.
- Se almacenan datos base de identificacion y contacto corporativo.
- La empresa queda habilitada para asociar proyectos SGSI.

## 2) Creacion de proyecto

- Se crea el proyecto SGSI vinculado a la empresa.
- Se define alcance inicial, fechas y responsables del proyecto.
- El proyecto centraliza fases, tareas, riesgos, documentos y trazabilidad.

## 3) Asignar contactos

- Se registran contactos de la empresa (roles de negocio y tecnicos).
- Se asocian contactos al proyecto mediante ProjectContact.
- Se validan reglas de consistencia (contacto y proyecto deben pertenecer a la misma empresa).

## 4) Registrar activos

- Se registran activos relevantes del proyecto (informacion, sistemas, infraestructura, procesos).
- Cada activo puede clasificarse por criticidad y propietario.
- Los activos sirven de base para controles, riesgos y evidencia documental.

## 5) Crear fases

- Se definen fases del proyecto (ej. diagnostico, planificacion, implementacion, verificacion, mejora).
- Las fases estructuran el trabajo por objetivos y periodos.
- Cada fase agrupa tareas y permite seguimiento de avance.

## 6) Crear tareas

- Se crean tareas operativas por fase.
- Las tareas tienen responsable, estado, fechas planificadas y fechas reales.
- El seguimiento de tareas permite medir cumplimiento y detectar desviaciones.

## 7) Subir documentos

- Se registran documentos de trabajo y evidencia (politicas, procedimientos, registros, reportes).
- Se validan estados y reglas de aprobacion cuando aplica.
- Los documentos respaldan el cumplimiento de requisitos ISO 27001.

## 8) Registrar auditoria

- El sistema registra eventos de auditoria (usuario, accion, entidad afectada, timestamp).
- La auditoria permite trazabilidad de cambios y control de integridad operativa.
- Esta evidencia se usa para revision interna y presentacion ante evaluacion externa.

## Resultado esperado

- Flujo SGSI trazable extremo a extremo.
- Coherencia entre modelo de datos, API y evidencia documental.
- Base lista para demo tecnica enfocada en backend.

## Relacion con arquitectura backend

El flujo descrito corresponde directamente al modelo de datos implementado en el backend,
siguiendo un enfoque database-first y arquitectura multi-tenant.

Cada entidad del flujo se encuentra representada en el modelo relacional,
con validaciones de integridad, restricciones y trazabilidad mediante auditoria.

Este flujo sirve como base para pruebas API, validacion funcional y demostracion tecnica.

## Estado PostgreSQL

- Modelo relacional alineado con el flujo SGSI documentado.
- Migraciones estructurales aplicadas y validadas en entorno local.
- Constraints de integridad implementados en entidades criticas.
- Pendiente operativo de Dia 3: validacion final en base limpia y checklist de despliegue.
