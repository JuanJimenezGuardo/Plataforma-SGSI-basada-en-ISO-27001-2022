# GUIA DE DEMOSTRACION EN VIVO - SPRINT 2
## VIT SGSI ISO 27001 (15-20 minutos)

---

## PREPARACION PREVIA

### 1. Levantar Backend

```bash
cd backend
venv\Scripts\activate
python manage.py runserver
```

Verificar salida esperada:
- Starting development server at http://127.0.0.1:8000/

### 2. Ejecutar Script de Demo Sprint 2

```bash
c:/Proyecto_VIT/.venv/Scripts/python.exe backend/tests/03_demo_sprint/demo_reunion_sprint2.py
```

- La demo es interactiva.
- En cada fase, presiona ENTER para avanzar.

### 3. Tener listos documentos de respaldo

- z_docs/03_engineering/backend/sprint_2/api_validation_day5.md
- z_docs/02_sprints/sprint_2/SPRINT2_QUICK_REFERENCE.md
- z_docs/02_sprints/ASIGNACIONES_SPRINT_ACTUALIZADO.md

---

## OBJETIVO DE LA REUNION

Demostrar cierre de Sprint 2 en backend con tres tipos de evidencia:
1. Evidencia visual (script en vivo).
2. Evidencia tecnica (validacion de API y estabilidad).
3. Evidencia formal (documentos de cierre y handoff a Sprint 3).

---

## DEMO EN VIVO (SECUENCIA RECOMENDADA)

### FASE 1: CARGA DE DATOS DEMO (2-3 min)

Que muestra:
- Usuarios por rol: ADMIN, CONSULTANT, CLIENT.
- Empresas demo: ACME y Bancolombia.
- Proyecto principal: Implementacion ISO 27001 - ACME.
- Entidades Sprint 2: Contact, ProjectContact, Phase, Task con work_notes y Document.

Mensaje recomendado:
"En esta fase preparo un escenario controlado y reproducible para demostrar Sprint 2 sin depender de datos manuales."

### FASE 2: HEALTH CHECK (1 min)

Que muestra:
- Conexion real ORM <-> base de datos (SELECT 1).

Mensaje recomendado:
"Antes de validar negocio, confirmamos salud tecnica del backend y su conectividad de datos."

### FASE 3: SEGURIDAD BASE SPRINT 1 (2-3 min)

Que muestra:
- Endpoints protegidos sin token (401).
- Control de roles RBAC (403 para accesos no permitidos).
- AuditLog activo.

Mensaje recomendado:
"Sprint 2 se apoya en una base segura ya cerrada: JWT, RBAC y trazabilidad de auditoria."

### FASE 4: CAMBIOS DE MODELO SPRINT 2 (3-4 min)

Que valida:
- Fechas planned/actual en Project, Phase y Task.
- Campo work_notes en Task.
- Eliminacion de campos legacy de contacto en Company.
- Conteo de entidades para verificar estructura real en BD.

Mensaje recomendado:
"Este fue el nucleo del sprint: evolucion del modelo para trazabilidad operativa real."

### FASE 5: API CORE SPRINT 2 (3 min)

Que muestra:
- Revision de endpoints core sin errores 500.
- Validacion con distintos roles para estabilidad general.

Mensaje recomendado:
"La capa REST quedo estable para integracion con frontend y siguientes modulos."

### FASE 6: CASO FUNCIONAL INTEGRAL (2-3 min)

Que muestra:
- Consulta de proyectos por rol.
- Contactos asociados al proyecto.
- ProjectContact operativo.
- Task con bitacora (work_notes).
- Documento de trazabilidad asociado al proyecto.

Mensaje recomendado:
"Aqui se ve el flujo funcional de negocio sobre el modelo nuevo."

### FASE 7: CIERRE EJECUTIVO (1 min)

Que muestra:
- Resumen de fases validadas.
- Resultado global.
- Siguiente paso: contrato API final + integracion frontend.

Mensaje recomendado:
"Con esto cerramos Sprint 2 en backend y dejamos listo el handoff de Sprint 3."

---

## RESPALDO TECNICO DESPUES DE LA DEMO

1. z_docs/03_engineering/backend/sprint_2/api_validation_day5.md
- Evidencia de validacion tecnica de endpoints.

2. z_docs/02_sprints/sprint_2/SPRINT2_QUICK_REFERENCE.md
- Estado de cierre tecnico y handoff.

3. z_docs/02_sprints/ASIGNACIONES_SPRINT_ACTUALIZADO.md
- Cumplimiento del plan de sprint.

---

## CHECKLIST ANTES DE ENTRAR A REUNION

- [ ] Backend corriendo en puerto 8000.
- [ ] Script demo_reunion_sprint2.py listo.
- [ ] Flujo ENTER por fases practicado una vez.
- [ ] Documentos de respaldo abiertos.
- [ ] Mensaje de cierre memorizado.

---

## MENSAJE FINAL RECOMENDADO

"Sprint 2 backend queda demostrado funcionalmente en vivo, y tecnicamente respaldado con validacion API y documentacion de cierre."
