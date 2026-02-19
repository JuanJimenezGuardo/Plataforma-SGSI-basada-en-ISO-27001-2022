# VIT — Plataforma Web para Implementación de SGSI ISO/IEC 27001

Documentación técnica del proyecto **VIT (Virtual ISMS Tool)**, una plataforma web para **implementar y operar un SGSI** alineado con **ISO/IEC 27001:2022**.

---

## Objetivo del proyecto

Construir una plataforma completa donde:

- Los usuarios se autentiquen con **3 roles**: **Administrador (Admin)**, **Consultor** y **Cliente**
- Los consultores creen **proyectos ISO 27001** con **fases** y **tareas**
- Se evalúen **riesgos** y se gestionen **controles del Anexo A**
- Se gestione **documentación y evidencias**
- Se generen **reportes de progreso** y trazabilidad de implementación

---

## Estado actual del proyecto (al 18-02-2026)

**Avance implementado (backend):** Users, Companies, Projects, Phases y Tasks operativos (API REST en Django + DRF).  
**Pendiente crítico (backend):** autenticación/autorización (JWT), núcleo SGSI (Scope, Asset, Risk, ISOControl, SoAItem, Evidence, Report) y auditoría completa.  
**Frontend:** existe la estructura base (Vite) pero aún no hay páginas ni componentes implementados.

**Próximos pasos inmediatos (prioridad):**
1. Activar **Auth/JWT** y permisos por rol/proyecto (RBAC + ProjectUser).
2. Implementar **Scope + Asset** y luego **Risk** (inherente/residual) con relación Risk↔Asset.
3. Cargar **ISOControl** (93 controles) y generar **SoA** por proyecto.
4. Implementar **Evidence** (subidas/estados) y **AuditLog** para trazabilidad.
5. Iniciar frontend con **Login**, rutas protegidas y vista básica de proyectos.



## Alcance funcional (alto nivel)

- **Autenticación y autorización por roles** (RBAC)
- **Gestión de compañías y proyectos** (cliente / consultor responsable)
- **Fases y tareas** por proyecto, con estados, prioridad y trazabilidad
- **Gestión de riesgos** (riesgo inherente y residual) + **activos**
- **Catálogo de controles ISO** (93 controles del Anexo A 27001:2022) y **SoA**
- **Evidencias** (archivos) y **documentos generados** (p. ej., reportes/SoA en PDF)
- **Auditoría y trazabilidad** (bitácora de eventos, historial de cambios, integridad)

---

## Stack propuesto

- **Backend**: Django + Django REST Framework
- **BD**: PostgreSQL
- **Frontend**: React + Vite (planeado)
- **Almacenamiento de archivos**: local/S3 (según despliegue)

---

## Documentos incluidos

- `RESUMEN_EJECUTIVO.md` — visión ejecutiva y backlog inicial
- `MODELO_DATOS_FORMAL.md` — modelo entidad–relación y tablas (formal)
- `DICCIONARIO_DATOS.md` — definiciones de campos, reglas y validaciones
- `CARDINALIDADES_RELACIONES.md` — relaciones y cardinalidades entre entidades
- `ARQUITECTURA_RIESGOS.md` — arquitectura de gestión de riesgos (ISO 27001)
- `ESTRATEGIA_AUDITORIA.md` — estrategia de trazabilidad/auditoría (alineación Anexo A)

---

## Nota de implementación

En los documentos se usa una **convención mixta**:
- Los **nombres de modelos/campos** se presentan en estilo técnico (compatibles con Django/BD).
- Las **descripciones y reglas** están en español para facilitar revisión académica y de negocio.
