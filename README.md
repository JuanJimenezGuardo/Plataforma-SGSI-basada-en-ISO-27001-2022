# VIT â€” Plataforma SGSI ISO 27001

**Plataforma web para implementaciÃ³n de Sistemas de GestiÃ³n de Seguridad de InformaciÃ³n (SGSI) basados en ISO 27001:2022**

---

## ðŸŽ¯ Objetivo del Proyecto

Permitir a empresas implementar ISO 27001 de forma estructurada, con gestiÃ³n de:
- Proyectos y fases de implementaciÃ³n
- IdentificaciÃ³n y anÃ¡lisis de riesgos
- Statement of Applicability (SoA)
- Carga y seguimiento de evidencias
- Reportes de conformidad

---

## ðŸ—ï¸ Arquitectura del Proyecto

**Este proyecto estÃ¡ diseÃ±ado con arquitectura de PRODUCCIÃ“N desde el Sprint 1**, no es un prototipo local.

### Stack TecnolÃ³gico Elegido

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚                     USERS (INTERNET)                         â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
            â”‚                                        â”‚
            â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                             â”‚
        â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
        â”‚                    â”‚                    â”‚
        â–¼                    â–¼                    â–¼
    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”      â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”      â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
    â”‚ Vercel  â”‚      â”‚Render Web APIâ”‚      â”‚ Render   â”‚
    â”‚ Frontendâ”‚â—„â”€â”€â”€â”€â–ºâ”‚  Django/DRF  â”‚â—„â”€â”€â”€â”€â–ºâ”‚PostgreSQLâ”‚
    â”‚ React   â”‚      â”‚  Gunicorn    â”‚      â”‚  DB      â”‚
    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜      â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜      â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                            â”‚
                            â–¼
                    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                    â”‚  S3 Storage  â”‚
                    â”‚  (Evidencias)â”‚
                    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

### Decisiones ArquitectÃ³nicas Clave

| DecisiÃ³n | TecnologÃ­a | Por quÃ© | Documento |
|----------|-----------|---------|-----------|
| **Backend** | Django + DRF | Framework maduro, SGSI requiere complejidad | SPRINT_1_GUIA_BACKEND.md |
| **Frontend** | React 18 + Vite | SPA moderno, responsive para mÃºltiples roles | (ImplementaciÃ³n Tinky) |
| **Hosting Backend** | Render | PostgreSQL administrada incluida, pricing predecible | ARQUITECTURA_DESPLIEGUE_PRODUCCION.md |
| **Hosting Frontend** | Vercel | IntegraciÃ³n GitHub, CDN global, cero config | ARQUITECTURA_DESPLIEGUE_PRODUCCION.md |
| **Base de Datos** | PostgreSQL 15 | SQL para relaciones complejas, SGSI data integrity crÃ­tica | ARQUITECTURA_DESPLIEGUE_PRODUCCION.md |
| **Almacenamiento Archivos** | S3 Compatible | Filesystem efÃ­mero en Render no funciona para archivos permanentes | ARQUITECTURA_DESPLIEGUE_PRODUCCION.md |
| **AutenticaciÃ³n** | JWT + SimpleJWT | Stateless, escalable multi-region | SPRINT_1_GUIA_BACKEND.md |
| **AutorizaciÃ³n** | Role-Based Access Control (RBAC) | SGSI requiere control fino: Admin/Consultant/Client | PLAN_EQUIPOS_SPRINT_1.md |
| **CI/CD** | GitHub Actions | AutomatizaciÃ³n tests + deploy, cero fricciÃ³n | ARQUITECTURA_DESPLIEGUE_PRODUCCION.md |

---

## ðŸ“… Timeline: 6 Sprints (18 feb â†’ 15 may 2026)

### âœ… Sprint 1 (19 feb - 2 mar): Auth + Security Base [COMPLETADO - v0.1-sprint1]
- âœ… User model (AbstractUser con roles: ADMIN, CONSULTANT, CLIENT)
- âœ… JWT authentication (SimpleJWT con access + refresh tokens)
- âœ… Role-based permissions (6 permission classes: IsAdmin, IsConsultant, IsClient, etc.)
- âœ… ProjectUser (user-project-role relationship con CRUD completo)
- âœ… AuditLog (modelo, serializer, viewset - registra QUIEN/QUE/CUANDO automÃ¡ticamente)
- âœ… Django signals (10 signal receivers para logging automÃ¡tico de cambios)
- âœ… Demo data + automated tests (backend/tests/03_demo_sprint/test_demo_sprint1.py valida 5 escenarios completos)

**Estado:** Backend 100% funcional. 7 endpoints protegidos, 3 roles trabajando, AuditLog registrando cambios automÃ¡ticamente.

**DecisiÃ³n de ProducciÃ³n:** Settings por entorno âœ…, JWT cookies seguras âœ…, CORS configurado âœ…, estructura production-ready âœ…

### Sprint 2 (3 - 16 mar): Scope + Assets
- Scope (alcance del SGSI)
- Asset inventory (quÃ© protegemos)
- Relaciones y validaciones BD

**DecisiÃ³n de ProducciÃ³n:** Migraciones reversibles, indexaciÃ³n, N+1 query prevention

### Sprint 3 (17 - 30 mar): Risk Assessment
- Risk identification
- Likelihood Ã— Impact matrix
- Automatic score calculation
- Risk mitigation tracking

**DecisiÃ³n de ProducciÃ³n:** CÃ¡lculos determinÃ­sticos, thread-safe signals, audit trail completo

### Sprint 4 (31 mar - 13 abr): SoA + ISO Controls
- 93 ISO 27001 controls
- Statement of Applicability
- Automatic SoA generation

**DecisiÃ³n de ProducciÃ³n:** Datos de referencia versionados, caching, textos validados

### Sprint 5 (14 - 27 abr): Evidence + Audit
- File upload (evidencias)
- Evidence tracking
- Complete audit trail

**DecisiÃ³n de ProducciÃ³n:** Almacenamiento persistente S3, validaciÃ³n archivos, virus scan (opcional)

### Sprint 6 (28 abr - 11 may): Reports + Dashboard
- Compliance metrics
- Risk dashboards
- Custom reports

**DecisiÃ³n de ProducciÃ³n:** Queries optimizadas, pagination, rate limiting, lazy aggregation

### Buffer (12 - 15 may): QA + Final Demo
- End-to-end testing
- Demo final
- Production readiness validation

---

## ðŸ“š Documentos del Proyecto

### 1. **PLAN_EQUIPOS_SPRINT_1.md**
Define roles y responsabilidades:
- Arquitecto + LÃ­der TÃ©cnico (diseÃ±o, code review, decisiones tech)
- Backend Implementador (CRUD endpoints, signals, tests)
- Frontend Developer (React components, UI, API calls)

Incluye:
- Reuniones (Lunes 30min, MiÃ©rcoles async, Viernes demo 45min)
- Governance (Git commits, PRs, demos como evidencia)
- Cultura de trabajo sin micromanagement

### 2. **ASIGNACIONES_SPRINT_1_A_6.md**
Desglose semana a semana de tareas con:
- Actividades por rol en cada sprint
- "Impacto en ProducciÃ³n" para cada sprint (decisiones tÃ©cnicas)
- Output esperado y mÃ©tricas
- Rojo/Amarillo/Verde por sprint

### 3. **SPRINT_1_GUIA_BACKEND.md**
Tutorial completo para Backend Implementador:
- Conceptos (AbstractUser, JWT, ProjectUser, AuditLog)
- 10 dÃ­as detallados (DÃ­a 1-10)
- Checkpoints de validaciÃ³n
- Errores comunes y soluciones

### 4. **CHECKLIST_SEMANAL_SPRINT_1.md**
ValidaciÃ³n semanal (Viernes):
- Preguntas tÃ©cnicas para cada rol
- SemÃ¡foro ðŸŸ¢/ðŸŸ¡/ðŸ”´
- FAQ y troubleshooting

### 5. **MONITOREO_SEMANAL.md**
Sistema de governance:
- Lunes: planificaciÃ³n
- MiÃ©rcoles: mid-week checkpoint
- Viernes: demo + validaciÃ³n tÃ©cnica
- Escaladra de problemas (bloqueadores)

### 6. **ARQUITECTURA_DESPLIEGUE_PRODUCCION.md** â­
**DOCUMENTO CLAVE**: Arquitectura transversal que condiciona TODO:
- Stack elegido (Render + Vercel + PostgreSQL + S3)
- Django production settings (DEBUG=False, HTTPS, etc)
- Variables de entorno
- Migraciones seguras
- CI/CD automÃ¡tico
- Costos ($27/mes MVP)
- Checklist pre-lanzamiento
- Riesgos y mitigaciÃ³n

---

## ðŸš€ Comienza AquÃ­

### Para Arquitecto/LÃ­der:
1. Leer [PLAN_EQUIPOS_SPRINT_1.md](PLAN_EQUIPOS_SPRINT_1.md) â€” tu rol
2. Revisar [ARQUITECTURA_DESPLIEGUE_PRODUCCION.md](ARQUITECTURA_DESPLIEGUE_PRODUCCION.md) â€” decisiones tech
3. Ejecutar reuniÃ³n Lunes 24 feb

### Para Backend Implementador:
1. Leer [SPRINT_1_GUIA_BACKEND.md](SPRINT_1_GUIA_BACKEND.md) â€” tu tutorial completo
2. Revisar [ARQUITECTURA_DESPLIEGUE_PRODUCCION.md](ARQUITECTURA_DESPLIEGUE_PRODUCCION.md) Â§ "ConfiguraciÃ³n Django"
3. Comenzar con abstractUser migration

### Para Frontend Developer:
1. Leer [PLAN_EQUIPOS_SPRINT_1.md](PLAN_EQUIPOS_SPRINT_1.md) â€” tu rol
2. Revisar [ASIGNACIONES_SPRINT_1_A_6.md](ASIGNACIONES_SPRINT_1_A_6.md) Sprint 1 secciÃ³n Frontend
3. Revisar setup React + conectar API (localhost:8000)

---

## ðŸ› ï¸ Setup Local

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

## ðŸ… Ã‰xito del Proyecto

Cada sprint tiene output claro:

| Sprint | ValidaciÃ³n | Evidencia |
|--------|-----------|----------|
| 1 | Auth funciona sin errores | Demo: Login â†’ Postman muestra tokens |
| 2 | Scope + Asset CRUD | Demo: Crear scope, listar assets |
| 3 | Risk con scoring automÃ¡tico | Demo: Crear risk, score calcula solo |
| 4 | 93 controlados mapeados, SoA generado | Demo: SoA lista todos los controles |
| 5 | Upload de archivos persistente | Demo: Subir evidencia, descarga correcta |
| 6 | Reportes generan correctamente | Demo: Dashboard con grÃ¡ficas |

---

## ðŸ“ž Contacto / Soporte

- **Bloqueadores tÃ©cnicos Sprint 1:** Respuesta < 4 horas
- **Decisiones arquitectÃ³nicas:** Revisar ARQUITECTURA_DESPLIEGUE_PRODUCCION.md primero
- **Reuniones:** Lunes 30min, Viernes 45min (obligatorias ambas)

---

## ðŸ“Š MÃ©tricas de Ã‰xito

**Sprint 1 (mÃ­nimo):**
- âœ… 3+ commits/persona/semana
- âœ… 1-2 PRs descriptivos/persona/semana
- âœ… Demo funcional viernes
- âœ… 0 errores de cÃ³digo muerto (flake8 + tests pasan)

**Global (6 sprints):**
- âœ… Arquitectura profesional (no improvisada)
- âœ… CI/CD automÃ¡tico
- âœ… CÃ³digo versionado en Git con historia limpia
- âœ… Deployment a Render sin manual work
- âœ… < 1% errores 500 en producciÃ³n

---

## ðŸ“– Referencias

- Django Docs: https://docs.djangoproject.com/en/4.2/
- DRF Docs: https://www.django-rest-framework.org/
- SimpleJWT: https://django-rest-framework-simplejwt.readthedocs.io/
- ISO 27001:2022: https://www.iso.org/standard/27001
- Render Docs: https://render.com/docs
- Vercel Docs: https://vercel.com/docs

---

**PrÃ³ximo paso:** ReuniÃ³n Lunes 24 feb @ 10 AM (30 min)  
**Estado:** Sprint 1 iniciando  
**Ãšltima actualizaciÃ³n:** 23 febrero 2026

