# Plataforma SGSI ISO 27001:2022 - Portafolio Publico

Proyecto academico orientado al diseno y desarrollo de una aplicacion web para apoyar la gestion de seguridad de la informacion en una organizacion, aplicando la norma ISO 27001:2022. La solucion permite organizar activos, riesgos, usuarios, controles y documentacion asociada al SGSI.

El desarrollo completo del proyecto se trabajo en un repositorio privado durante el proceso academico. Esta version publica muestra la arquitectura, componentes implementados, evidencia tecnica y una muestra representativa del trabajo.

---

## Objetivo del Proyecto

Construir una plataforma para apoyar a organizaciones en la implementacion de ISO 27001, con modulos para:
- Gestion de proyectos y fases
- Gestion de tareas y responsables
- Base de autenticacion y permisos por rol
- Trazabilidad y auditoria de eventos
- Base para riesgos, controles y evidencia documental

## Alcance de Esta Version Publica

- Se mantiene codigo y documentacion tecnica utiles para evaluacion profesional
- No se publica informacion sensible ni configuraciones privadas
- El repositorio se enfoca en demostrar diseno, implementacion y criterio tecnico

## Mi Rol

- Liderazgo y coordinacion tecnica del proyecto
- Definicion de alcance, arquitectura y plan de sprints
- Desarrollo de funcionalidades backend y soporte a integracion frontend
- Seguimiento de entregables, calidad tecnica y evidencia de avance

---

## 🏗️ Arquitectura del Proyecto

**Este proyecto está diseñado con arquitectura de PRODUCCIÓN desde el Sprint 1**, no es un prototipo local.

### Stack Tecnológico Elegido

```
┌─────────────────────────────────────────────────────────────┐
│                     USERS (INTERNET)                         │
└─────────────────────────────────────────────────────────────┘
            │                                        │
            └────────────────┬───────────────────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
    ┌─────────┐      ┌──────────────┐      ┌──────────┐
    │ Vercel  │      │Render Web API│      │ Render   │
    │ Frontend│◄────►│  Django/DRF  │◄────►│PostgreSQL│
    │ React   │      │  Gunicorn    │      │  DB      │
    └─────────┘      └──────────────┘      └──────────┘
                            │
                            ▼
                    ┌──────────────┐
                    │  S3 Storage  │
                    │  (Evidencias)│
                    └──────────────┘
```

### Decisiones Arquitectónicas Clave

| Decisión | Tecnología | Por qué | Documento |
|----------|-----------|---------|-----------|
| **Backend** | Django + DRF | Framework maduro, SGSI requiere complejidad | SPRINT_1_GUIA_BACKEND.md |
| **Frontend** | React 18 + Vite | SPA moderno, responsive para múltiples roles | (Implementación Tinky) |
| **Hosting Backend** | Render | PostgreSQL administrada incluida, pricing predecible | ARQUITECTURA_DESPLIEGUE_PRODUCCION.md |
| **Hosting Frontend** | Vercel | Integración GitHub, CDN global, cero config | ARQUITECTURA_DESPLIEGUE_PRODUCCION.md |
| **Base de Datos** | PostgreSQL 15 | SQL para relaciones complejas, SGSI data integrity crítica | ARQUITECTURA_DESPLIEGUE_PRODUCCION.md |
| **Almacenamiento Archivos** | S3 Compatible | Filesystem efímero en Render no funciona para archivos permanentes | ARQUITECTURA_DESPLIEGUE_PRODUCCION.md |
| **Autenticación** | JWT + SimpleJWT | Stateless, escalable multi-region | SPRINT_1_GUIA_BACKEND.md |
| **Autorización** | Role-Based Access Control (RBAC) | SGSI requiere control fino: Admin/Consultant/Client | PLAN_EQUIPOS_SPRINT_1.md |
| **CI/CD** | GitHub Actions | Automatización tests + deploy, cero fricción | ARQUITECTURA_DESPLIEGUE_PRODUCCION.md |

---

## 📅 Timeline: 6 Sprints (18 feb → 15 may 2026)

### ✅ Sprint 1 (19 feb - 2 mar): Auth + Security Base [COMPLETADO - v0.1-sprint1]
- ✅ User model (AbstractUser con roles: ADMIN, CONSULTANT, CLIENT)
- ✅ JWT authentication (SimpleJWT con access + refresh tokens)
- ✅ Role-based permissions (6 permission classes: IsAdmin, IsConsultant, IsClient, etc.)
- ✅ ProjectUser (user-project-role relationship con CRUD completo)
- ✅ AuditLog (modelo, serializer, viewset - registra QUIEN/QUE/CUANDO automáticamente)
- ✅ Django signals (10 signal receivers para logging automático de cambios)
- ✅ Demo data + automated tests (backend/tests/test_demo_sprint1.py valida 5 escenarios completos)

**Estado:** Backend 100% funcional. 7 endpoints protegidos, 3 roles trabajando, AuditLog registrando cambios automáticamente.

**Decisión de Producción:** Settings por entorno ✅, JWT cookies seguras ✅, CORS configurado ✅, estructura production-ready ✅

### Sprint 2 (3 - 16 mar): Scope + Assets
- Scope (alcance del SGSI)
- Asset inventory (qué protegemos)
- Relaciones y validaciones BD

**Decisión de Producción:** Migraciones reversibles, indexación, N+1 query prevention

### Sprint 3 (17 - 30 mar): Risk Assessment
- Risk identification
- Likelihood × Impact matrix
- Automatic score calculation
- Risk mitigation tracking

**Decisión de Producción:** Cálculos determinísticos, thread-safe signals, audit trail completo

### Sprint 4 (31 mar - 13 abr): SoA + ISO Controls
- 93 ISO 27001 controls
- Statement of Applicability
- Automatic SoA generation

**Decisión de Producción:** Datos de referencia versionados, caching, textos validados

### Sprint 5 (14 - 27 abr): Evidence + Audit
- File upload (evidencias)
- Evidence tracking
- Complete audit trail

**Decisión de Producción:** Almacenamiento persistente S3, validación archivos, virus scan (opcional)

### Sprint 6 (28 abr - 11 may): Reports + Dashboard
- Compliance metrics
- Risk dashboards
- Custom reports

**Decisión de Producción:** Queries optimizadas, pagination, rate limiting, lazy aggregation

### Buffer (12 - 15 may): QA + Final Demo
- End-to-end testing
- Demo final
- Production readiness validation

---

## 📚 Documentos del Proyecto

### 1. **PLAN_EQUIPOS_SPRINT_1.md**
Define roles y responsabilidades:
- Arquitecto + Líder Técnico (diseño, code review, decisiones tech)
- Backend Implementador (CRUD endpoints, signals, tests)
- Frontend Developer (React components, UI, API calls)

Incluye:
- Reuniones (Lunes 30min, Miércoles async, Viernes demo 45min)
- Governance (Git commits, PRs, demos como evidencia)
- Cultura de trabajo sin micromanagement

### 2. **ASIGNACIONES_SPRINT_1_A_6.md**
Desglose semana a semana de tareas con:
- Actividades por rol en cada sprint
- "Impacto en Producción" para cada sprint (decisiones técnicas)
- Output esperado y métricas
- Rojo/Amarillo/Verde por sprint

### 3. **SPRINT_1_GUIA_BACKEND.md**
Tutorial completo para Backend Implementador:
- Conceptos (AbstractUser, JWT, ProjectUser, AuditLog)
- 10 días detallados (Día 1-10)
- Checkpoints de validación
- Errores comunes y soluciones

### 4. **CHECKLIST_SEMANAL_SPRINT_1.md**
Validación semanal (Viernes):
- Preguntas técnicas para cada rol
- Semáforo 🟢/🟡/🔴
- FAQ y troubleshooting

### 5. **MONITOREO_SEMANAL.md**
Sistema de governance:
- Lunes: planificación
- Miércoles: mid-week checkpoint
- Viernes: demo + validación técnica
- Escaladra de problemas (bloqueadores)

### 6. **ARQUITECTURA_DESPLIEGUE_PRODUCCION.md** ⭐
**DOCUMENTO CLAVE**: Arquitectura transversal que condiciona TODO:
- Stack elegido (Render + Vercel + PostgreSQL + S3)
- Django production settings (DEBUG=False, HTTPS, etc)
- Variables de entorno
- Migraciones seguras
- CI/CD automático
- Costos ($27/mes MVP)
- Checklist pre-lanzamiento
- Riesgos y mitigación

---

## 🚀 Comienza Aquí

### Para Arquitecto/Líder:
1. Leer [PLAN_EQUIPOS_SPRINT_1.md](PLAN_EQUIPOS_SPRINT_1.md) — tu rol
2. Revisar [ARQUITECTURA_DESPLIEGUE_PRODUCCION.md](ARQUITECTURA_DESPLIEGUE_PRODUCCION.md) — decisiones tech
3. Ejecutar reunión Lunes 24 feb

### Para Backend Implementador:
1. Leer [SPRINT_1_GUIA_BACKEND.md](SPRINT_1_GUIA_BACKEND.md) — tu tutorial completo
2. Revisar [ARQUITECTURA_DESPLIEGUE_PRODUCCION.md](ARQUITECTURA_DESPLIEGUE_PRODUCCION.md) § "Configuración Django"
3. Comenzar con abstractUser migration

### Para Frontend Developer:
1. Leer [PLAN_EQUIPOS_SPRINT_1.md](PLAN_EQUIPOS_SPRINT_1.md) — tu rol
2. Revisar [ASIGNACIONES_SPRINT_1_A_6.md](ASIGNACIONES_SPRINT_1_A_6.md) Sprint 1 sección Frontend
3. Revisar setup React + conectar API (localhost:8000)

---

## 🛠️ Setup Local

### Backend

```bash
cd backend

# Virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Create .env (copy from .env.example)
cp .env.example .env

# Migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run
python manage.py runserver
# Opens on http://localhost:8000/
```

### Frontend

```bash
cd frontend

npm install
npm run dev
# Opens on http://localhost:3000/
```

## Pruebas: Suite Formal vs Demo de Sprint

Para evitar confusiones en revision tecnica y sustentacion, el repositorio maneja dos tipos de pruebas.

### 1) Suite formal (unitarias/integracion por app)

- Ubicacion: `backend/apps/*/tests/`
- Uso: calidad tecnica, validacion reproducible, ejecucion tipo CI

```bash
cd backend
python manage.py test apps.users.tests apps.companies.tests apps.projects.tests apps.phases.tests apps.tasks.tests
```

### 2) Scripts de validacion funcional (evidencia de sprint)

- Ubicacion: `backend/tests_demo/`
- Uso: demostraciones funcionales guiadas (no forman parte de la suite formal)

```bash
cd backend
python tests_demo/test_demo_sprint1.py
```

Tambien puedes ejecutar otros scripts de demo en esa misma carpeta segun el escenario de presentacion.

---

## 🏅 Éxito del Proyecto

Cada sprint tiene output claro:

| Sprint | Validación | Evidencia |
|--------|-----------|----------|
| 1 | Auth funciona sin errores | Demo: Login → Postman muestra tokens |
| 2 | Scope + Asset CRUD | Demo: Crear scope, listar assets |
| 3 | Risk con scoring automático | Demo: Crear risk, score calcula solo |
| 4 | 93 controlados mapeados, SoA generado | Demo: SoA lista todos los controles |
| 5 | Upload de archivos persistente | Demo: Subir evidencia, descarga correcta |
| 6 | Reportes generan correctamente | Demo: Dashboard con gráficas |

---

## 📞 Contacto / Soporte

- **Bloqueadores técnicos Sprint 1:** Respuesta < 4 horas
- **Decisiones arquitectónicas:** Revisar ARQUITECTURA_DESPLIEGUE_PRODUCCION.md primero
- **Reuniones:** Lunes 30min, Viernes 45min (obligatorias ambas)

---

## 📊 Métricas de Éxito

**Sprint 1 (mínimo):**
- ✅ 3+ commits/persona/semana
- ✅ 1-2 PRs descriptivos/persona/semana
- ✅ Demo funcional viernes
- ✅ 0 errores de código muerto (flake8 + tests pasan)

**Global (6 sprints):**
- ✅ Arquitectura profesional (no improvisada)
- ✅ CI/CD automático
- ✅ Código versionado en Git con historia limpia
- ✅ Deployment a Render sin manual work
- ✅ < 1% errores 500 en producción

---

## 📖 Referencias

- Django Docs: https://docs.djangoproject.com/en/4.2/
- DRF Docs: https://www.django-rest-framework.org/
- SimpleJWT: https://django-rest-framework-simplejwt.readthedocs.io/
- ISO 27001:2022: https://www.iso.org/standard/27001
- Render Docs: https://render.com/docs
- Vercel Docs: https://vercel.com/docs

---

**Próximo paso:** Reunión Lunes 24 feb @ 10 AM (30 min)  
**Estado:** Sprint 1 iniciando  
**Última actualización:** 23 febrero 2026
