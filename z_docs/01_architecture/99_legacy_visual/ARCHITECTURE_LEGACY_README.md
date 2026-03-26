# VIT â€” Plataforma Web para ImplementaciÃ³n de SGSI ISO/IEC 27001

DocumentaciÃ³n tÃ©cnica del proyecto **VIT (Virtual ISMS Tool)**, una plataforma web para **implementar y operar un SGSI** alineado con **ISO/IEC 27001:2022**.

---

## Objetivo del proyecto

Construir una plataforma completa donde:

- Los usuarios se autentiquen con **3 roles**: **Administrador (Admin)**, **Consultor** y **Cliente**
- Los consultores creen **proyectos ISO 27001** con **fases** y **tareas**
- Se evalÃºen **riesgos** y se gestionen **controles del Anexo A**
- Se gestione **documentaciÃ³n y evidencias**
- Se generen **reportes de progreso** y trazabilidad de implementaciÃ³n

---

## Estado actual del proyecto (al 4 marzo 2026)

**âœ… SPRINT 1 COMPLETADO (v0.1-sprint1):**
- âœ… User model con AbstractUser (3 roles: ADMIN, CONSULTANT, CLIENT)
- âœ… JWT authentication (SimpleJWT implementado, tokens generados)
- âœ… Permisos por rol/proyecto (RBAC + ProjectUser con 6 permission classes)
- âœ… AuditLog con Django signals (registro automÃ¡tico de QUIEN/QUE/CUANDO)
- âœ… Companies, Projects, Phases, Tasks (CRUD completo)
- âœ… Demo data population (backend/scripts/populate_demo_data.py)
- âœ… Test suite automatizado (backend/tests/03_demo_sprint/test_demo_sprint1.py: 5 escenarios validados)
- âœ… Git: Commit tagged v0.1-sprint1, historial limpio

**PrÃ³ximos pasos inmediatos (Sprint 2-6):**
1. **Sprint 2:** Implementar **Scope + Asset** (alcance del SGSI e inventarios)
2. **Sprint 3:** Implementar **Risk** (riesgos inherente/residual con cÃ¡lculo automÃ¡tico)
3. **Sprint 4:** Cargar **ISOControl** (93 controles) y generar **SoA** automÃ¡tico
4. **Sprint 5:** Implementar **Evidence** (carga/versioning/aprobaciÃ³n)
5. **Sprint 6:** Reports + Dashboards
6. **Frontend:** React + Vite (Login, PrivateRoute, dashboards por rol)



## Alcance funcional (alto nivel)

- **AutenticaciÃ³n y autorizaciÃ³n por roles** (RBAC)
- **GestiÃ³n de compaÃ±Ã­as y proyectos** (cliente / consultor responsable)
- **Fases y tareas** por proyecto, con estados, prioridad y trazabilidad
- **GestiÃ³n de riesgos** (riesgo inherente y residual) + **activos**
- **CatÃ¡logo de controles ISO** (93 controles del Anexo A 27001:2022) y **SoA**
- **Evidencias** (archivos) y **documentos generados** (p. ej., reportes/SoA en PDF)
- **AuditorÃ­a y trazabilidad** (bitÃ¡cora de eventos, historial de cambios, integridad)

---

## Stack propuesto

- **Backend**: Django + Django REST Framework
- **BD**: PostgreSQL
- **Frontend**: React + Vite (planeado)
- **Almacenamiento de archivos**: local/S3 (segÃºn despliegue)

---

## Documentos incluidos

- `RESUMEN_EJECUTIVO.md` â€” visiÃ³n ejecutiva y backlog inicial
- `MODELO_DATOS_FORMAL.md` â€” modelo entidadâ€“relaciÃ³n y tablas (formal)
- `DICCIONARIO_DATOS.md` â€” definiciones de campos, reglas y validaciones
- `CARDINALIDADES_RELACIONES.md` â€” relaciones y cardinalidades entre entidades
- `ARQUITECTURA_RIESGOS.md` â€” arquitectura de gestiÃ³n de riesgos (ISO 27001)
- `ESTRATEGIA_AUDITORIA.md` â€” estrategia de trazabilidad/auditorÃ­a (alineaciÃ³n Anexo A)

---

## Nota de implementaciÃ³n

En los documentos se usa una **convenciÃ³n mixta**:
- Los **nombres de modelos/campos** se presentan en estilo tÃ©cnico (compatibles con Django/BD).
- Las **descripciones y reglas** estÃ¡n en espaÃ±ol para facilitar revisiÃ³n acadÃ©mica y de negocio.


