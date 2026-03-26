# ðŸŽ¯ VIT: RESUMEN EJECUTIVO PARA DESARROLLO

## Â¿QUÃ‰ ES VIT EN UNA FRASE?
**Plataforma web para que empresas implementen ISO 27001 de forma estructurada, automatizando riesgos, controles, evidencias y generando reportes de cumplimiento.**

---

## ðŸ‘¥ 3 ROLES CON PERMISOS DIFERENTES

| Rol | QuiÃ©n | Acceso | Acciones Principales |
|-----|-------|--------|----------------------|
| **ADMIN** | Personal VIT | Todos empresa/proyectos | Crear usuarios, crear empresas, ver auditorÃ­a global, aprobar evidencias |
| **CONSULTANT** | Consultor ISO | Proyectos asignados | Crear proyecto, evaluar riesgos, llenar SoA, revisar evidencias, generar reportes |
| **CLIENT** | Empresa cliente | Su empresa/proyectos | Ver progreso, cargar evidencias, confirmar SoA, ver reportes |

---

## ðŸŽ¬ CICLO COMPLETO DE UN PROYECTO (6 FASES)

### **F0: INICIO (1-2 semanas)**
- Admin crea Empresa
- Consultant se asigna al proyecto
- VIT auto-genera 5 fases + 93 items SoA

### **F1: CONTEXTO Y ALCANCE (3-4 semanas)**
- Consultant define Scope (sistemas in/out)
- Guarda quÃ© sistemas estÃ¡n en alcance

### **F2: RIESGOS Y CONTROLES (6-8 semanas)** â­
- Consultant crea 150-300 riesgos (Prob 1-5 + Impact 1-5 = score)
- Para cada riesgo: selecciona N controles mitigantes
- VIT auto-calcula score residual (despuÃ©s de controles)
- 93 items SoA cambian a IN_PROGRESS
- **KPI**: % de riesgos mitigados

### **F3: IMPLEMENTACIÃ“N Y OPERACIÃ“N (8-12 semanas)** â­
- Cliente carga evidencias (PDF, DOCX, etc.)
- Consultant revisa y aprueba/rechaza evidencias
- SoA items se marcan como IMPLEMENTED
- **KPI**: % de controles implementados

### **F4: EVALUACIÃ“N Y MEJORA (4-6 semanas)**
- AuditorÃ­a interna
- Acciones correctivas
- RevisiÃ³n direcciÃ³n
- **KPI**: % de acciones cerradas

### **F5: READINESS (1-2 semanas)**
- ValidaciÃ³n final
- Todas evidencias cargadas âœ…
- Todos controles implementados âœ…
- Exporta SoA final + AuditorÃ­a â†’ auditor externo

---

## ðŸ“Š LOS 12 REQUERIMIENTOS FUNCIONALES PRINCIPALES

| RF # | Nombre | QuÃ© Hace | Usuarios |
|------|--------|----------|----------|
| **RF1** | AutenticaciÃ³n JWT | Login â†’ tokens (access + refresh) | Todos |
| **RF2** | GestiÃ³n de Empresas | CRUD empresas cliente | Admin |
| **RF3** | GestiÃ³n de Proyectos | Crear/editar proyectos, auto-gen 5 fases | Admin, Consultant |
| **RF4** | GestiÃ³n Fases/Tareas | CRUD tareas, cambiar estado (%, fecha) | Consultant, Client |
| **RF5** | Scope & Activos | Definir alcance, inventario 50-200 activos | Consultant |
| **RF6** | Riesgos (Dual) | Crear riesgos, calcular inherente/residual, vincular controles | Consultant |
| **RF7** | SoA (93 Controles) | 93 items automÃ¡ticos, marcar aplicables/no aplicables, justificar | Consultant, Client |
| **RF8** | Evidencias | Subir archivos, versioning, estado (PENDING/APPROVED/REJECTED), comentarios | Client, Consultant |
| **RF9** | Reportes | Generar SoA PDF, matriz riesgos, % cumplimiento, reporte ejecutivo | Consultant |
| **RF10** | AuditorÃ­a (AuditLog) | Registro inmutable: QUIEN/QUE/CUANDO/DONDE, exportar para auditor externo | Admin, Consultant |
| **RF11** | Dashboard & KPIs | % proyecto, % riesgos mitigados, % controles implementados, grÃ¡ficas | Todos |
| **RF12** | Notificaciones | Alertas de tareas vencidas, evidencias rechazadas, cambios crÃ­ticos | Todos (future) |

---

## ðŸ—„ï¸ ENTIDADES CLAVE DEL MODELO

```
User (username, email, role: ADMIN/CONSULTANT/CLIENT)
â”œâ”€â”€ ProjectUser (un usuario puede tener diferentes roles en diferentes proyectos)
â”‚
Company (name, RFC, contacto, direcciÃ³n)
â”œâ”€â”€ Project (name, status, dates, created_by)
â”‚  â”œâ”€â”€ Phase (INIT, PLAN, IMPLEMENT, MAINTAIN, CERTIFY) Ã— 5
â”‚  â”‚  â””â”€â”€ Task (tÃ­tulo, status, responsable, fecha vencimiento)
â”‚  â”‚
â”‚  â”œâ”€â”€ Scope (sistemas in-scope, exclusiones, justificaciÃ³n)
â”‚  â”‚
â”‚  â”œâ”€â”€ Asset (hardware, software, data, personal, facility) Ã— 50-200
â”‚  â”‚  â””â”€ Risk (description, Prob 1-5, Impact 1-5) Ã— 150-300
â”‚  â”‚     â”œâ”€ Inherent Score = Prob Ã— Impact (auto)
â”‚  â”‚     â”œâ”€ Residual Score = Prob Ã— Impact (post-controles, auto)
â”‚  â”‚     â””â”€ Linked to ISOControl (N:M)
â”‚  â”‚
â”‚  â”œâ”€â”€ SoAItem Ã— 93 (1 por control ISO)
â”‚  â”‚  â”œâ”€â”€ is_applicable (SI/NO)
â”‚  â”‚  â”œâ”€â”€ justification (si no aplica)
â”‚  â”‚  â”œâ”€â”€ impl_status (NOT_IMPL â†’ IN_PROGRESS â†’ IMPLEMENTED)
â”‚  â”‚  â””â”€â”€ Evidence (versioning, approval workflow)
â”‚  â”‚
â”‚  â””â”€â”€ Document (SoA generada, reportes, auditorÃ­a)
â”‚
ISOControl Ã— 93 (A.5.1 â†’ A.9.7, read-only, precargado)
â”‚
AuditLog (QUIEN/QUE/CUANDO/DONDE)
```

---

## âš™ï¸ PROCESOS CRÃTICOS (WORKFLOWS)

### **Workflow 1: EvaluaciÃ³n de Riesgo**
```
1. Consultant crea Risk: "Acceso no autorizado a BD"
2. Ingresa: Prob=5, Impact=5 â†’ Score Inherente = 25 (auto)
3. Selecciona 3 controles: A.5.15, A.8.24, A.6.3
4. Ingresa: Prob residual=2 â†’ Score Residual = 10 (auto)
5. Efectividad = 25-10 = 15 (KPI)
6. VIT automÃ¡ticamente actualiza SoA items de esos 3 controles a IN_PROGRESS
7. AuditLog registra cada cambio: "Consultant#1 UPDATED Risk#5, changed Prob from 5 to 2"
```

### **Workflow 2: Carga de Evidencia y AprobaciÃ³n**
```
1. Client sube archivo: "Backup-Procedure-v2.pdf" para control A.5.18
2. VIT: create Evidence, version=2, status=PENDING
3. Consultant ve evidencia, descarga PDF, lee, comenta "Falta auditorÃ­a interna"
4. Client lee comentario, sube "Backup-Procedure-v3.pdf"
5. VIT: create Evidence, version=3, status=PENDING, links anterior (v2 â†’ v3)
6. Consultant aprueba: Evidence.status = APPROVED
7. VIT automÃ¡ticamente cambia SoAItem.impl_status = IMPLEMENTED
8. AuditLog registra: 
   - "Client#3 UPLOADED Evidence (version 2 for A.5.18)"
   - "Client#3 UPLOADED Evidence (version 3 for A.5.18)"
   - "Consultant#1 APPROVED Evidence (version 3 for A.5.18)"
```

### **Workflow 3: GeneraciÃ³n de Reporte SoA**
```
1. Consultant hace clic "Generar SoA"
2. VIT recorre 93 SoAItem del proyecto:
   - Si is_applicable=NO: muestra "No Aplicable - JustificaciÃ³n"
   - Si is_applicable=YES: muestra estado (NOT_IMPL, IN_PROGRESS, IMPLEMENTED)
   - Si IMPLEMENTED: adjunta evidencias aprobadas
3. Genera PDF de 20+ pÃ¡ginas: "SoA-Proyecto-VIT-2026-02.pdf"
4. Guardada en Document y disponible para descargar
5. Cliente descarga para auditor externo
6. AuditLog: "Consultant#1 GENERATED Report SoA for Project#5"
```

---

## ðŸ”’ SEGURIDAD Y AUDITORÃA

### **AuditLog: Lo que Se Registra TODO**
- **QUIEN**: User que hizo la acciÃ³n + IP + User-Agent
- **QUÃ‰**: Action (CREATE/UPDATE/DELETE/APPROVE), Entity (Risk, SoA, Evidence), cambios before/after (JSON)
- **CUÃNDO**: Timestamp UTC
- **DÃ“NDE**: Entidad especÃ­fica (Project#5, SoAItem#47, Evidence#123)
- **RESULTADO**: SUCCESS/FAIL

**Casos de uso de auditorÃ­a**:
- Admin filtra: "Mostrame todos los cambios a SoA en Ãºltimos 7 dÃ­as por Carlos"
- Auditor externo descarga: AuditLog completo del proyecto para verificar trazabilidad
- DetecciÃ³n: "3 riesgos eliminados en 30 minutos" â†’ investigar

### **Permisos por Rol (Ejemplo)**
```javascript
// Backend: Permisos en viewset
class RiskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsConsultantOrReadOnly]  // Consultant crea, Client ve
    
    def create(self, request):
        if request.user.role != 'CONSULTANT':
            return 403 Forbidden
        risk = Risk.objects.create(..., created_by=request.user)
        AuditLog.objects.create(action='CREATE', entity='Risk', object_id=risk.id, user=request.user)
        return 201 Created

// Frontend: Mostrar/ocultar UI
{user.role === 'CONSULTANT' && <button>Crear Riesgo</button>}
```

---

## ðŸ“± INTERFACES PRINCIPALES (FRONTEND)

| PÃ¡gina | Usuarios | QuÃ© Muestra | Acciones |
|--------|----------|------------|----------|
| **Dashboard** | Todos | % proyecto, % riesgos mitigados, % controles, prÃ³ximas tareas, grÃ¡ficas | Ver detalles |
| **Mis Proyectos** | Todos | Lista de proyectos + estado | Entrar/editar/crear |
| **Detalle Proyecto** | Todos | Fases, tareas, progreso, Ãºltimos cambios | Drilldown en fases |
| **Riesgos** | Consultant | Matriz 5Ã—5 (Prob vs Impact), tabla completa, filtros | Crear, editar, eliminar, vincular controles |
| **SoA** | Todos | Tabla 93 controles, estado, justificaciÃ³n, responsable, evidencias | Marcar aplicable, cargar evidencia, comentar |
| **Evidencias** | Client/Consultant | Grid de evidencias por SoA, versiones, estados, comentarios | Subir, descargar, revisar, comentar, aprobar |
| **Reportes** | Consultant | Lista de reportes generados, fecha, tipo | Generar nuevos, descargar PDF/Excel, ver historial |
| **AuditorÃ­a** | Admin | Tabla AuditLog con filtros (usuario, acciÃ³n, entidad, fecha) | Filtrar, exportar CSV/JSON, ver detalles |

---

## ðŸŽ¯ DATOS DE PRUEBA PARA DEMO (Semana 2)

Para demostrar el viernes, necesitas:

```sql
-- 1 Admin (VIT)
User: id=1, username="admin", role="ADMIN"

-- 1 Consultant (responsable proyecto)
User: id=2, username="carlos", role="CONSULTANT"

-- 2 Clients (empresa)
User: id=3, username="juan", role="CLIENT"
User: id=4, username="maria", role="CLIENT"

-- 1 Empresa
Company: id=1, name="Bancolombia S.A.", tax_id="860001022"

-- 1 Proyecto
Project: id=1, company=1, name="ISO 27001 Bancolombia", status="IN_PROGRESS", created_by=2

-- 5 Fases (auto-generadas)
Phase: F0, F1, F2, F3, F4 (status, % completado)

-- 3 Tareas (en fases diferentes)
Task: id=1, phase=2, title="Definir Scope", status="COMPLETED"
Task: id=2, phase=3, title="Crear 50 Activos", status="IN_PROGRESS"
Task: id=3, phase=3, title="Evaluar Riesgos", status="IN_PROGRESS"

-- 3 Riesgos (con inherente/residual)
Risk: id=1, project=1, name="Acceso no auth a BD", 
      inherent_prob=5, inherent_impact=5, inherent_score=25,
      residual_prob=2, residual_impact=5, residual_score=10,
      status="MITIGATED"

Risk: id=2, project=1, name="Malware en endpoints", 
      inherent_prob=4, inherent_impact=4, inherent_score=16,
      residual_prob=1, residual_impact=4, residual_score=4,
      status="MITIGATED"

-- 10 SoAItems (de 93 controles)
SoAItem: id=1, control=A.5.1, is_applicable=YES, impl_status="IMPLEMENTED"
SoAItem: id=2, control=A.5.2, is_applicable=NO, impl_status=NULL, justification="No aplica a empresa"
... (otros 8)

-- 5 Evidencias (varias versiones)
Evidence: id=1, soaitem=1, version=1, status="PENDING", uploaded_by=3 (juan)
Evidence: id=2, soaitem=1, version=2, status="APPROVED", uploaded_by=3, approved_by=2 (carlos)

-- 10 AuditLog (demostrar trazabilidad)
AuditLog: action="CREATE", entity="Project", user=2 (carlos), timestamp=2026-02-23
AuditLog: action="UPDATE", entity="Risk", user=2 (carlos), changes={"inherent_prob": [5, 4]}, timestamp=2026-02-24
... (otros 8)

-- ProjectUser (asignaciones)
ProjectUser: user=2 (carlos), project=1, role="CONSULTANT"
ProjectUser: user=3 (juan), project=1, role="CLIENT"
ProjectUser: user=4 (maria), project=1, role="CLIENT"
```

---

## ðŸš€ IMPLEMENTACIÃ“N SPRINT 1-4 (ROADMAP)

### **SPRINT 1 (19 feb - 2 mar): BASE DE SEGURIDAD** âœ… COMPLETADO (v0.1-sprint1)
- âœ… User AbstractUser + JWT (Auth backends, token validation)
- âœ… 6 permission classes (IsAdmin, IsConsultant, IsClient, IsAdminOrReadOnly, IsConsultantOrReadOnly, IsOwnerOrReadOnly)
- âœ… AuditLog + signals (Auto-logging de cambios, 10 signal receivers)
- âœ… Serializers/viewsets completos (7 viewsets con CRUD, filtering por rol)
- âœ… Demo data population (3 users, 2 companies, 2 projects, ProjectUser assignments)
- âœ… Pruebas automatizadas (backend/tests/03_demo_sprint/test_demo_sprint1.py: 5 escenarios validados)
- â³ Frontend Login + PrivateRoute (PrÃ³ximo: Sprint Frontend)

### **SPRINT 2 (3-16 mar): PROYECTOS + TAREAS**
- Crear/listar/editar proyectos
- Auto-generar 5 fases
- CRUD tareas + estado
- TaskViewSet con permisos por rol

### **SPRINT 3 (17-30 mar): RIESGOS**
- Risk model (inherent/residual, auto-calc scores)
- Risk â†” ISOControl (N:M)
- Risk matrix (Prob vs Impact, 5Ã—5)
- Dashboard riesgos

### **SPRINT 4 (31 mar-13 abr): SoA + EVIDENCIAS**
- SoA auto-generate (93 items)
- Evidence upload/versioning/approval workflow
- Dashboard SoA (% implementado)
- AuditorÃ­a de evidencias

---

## ðŸ“¦ ARCHIVOS INCLUIDOS EN REFERENCIAS

He copiado toda la documentaciÃ³n a `C:\Proyecto_VIT\REFERENCIAS_ISO27001\`:

- **Docs/**: 
  - `REQUERIMIENTOS FUNCIONALES (RF).docx` â† Lee esto primero
  - `Diagram_of_ISO_27001**.pdf` â† Fases visuales
  - `ISO 27001-2022.pdf` â† Referencia ISO

- **Implementacion/**: 
  - `Guia_Paso_a_Paso_ISO27001_VIT.docx` â† CÃ³mo implementar
  - `F0_Inicio.pptx` a `F5_Readiness.pptx` â† Presentaciones por fase
  - `Plantillas_SGSI_VIT_v2.xlsx` â† Templates uso
  - `SoA_Cookbook_Ejemplos.xlsx` â† Ejemplos SoA
  - `Acciones_Tecnologicas_Checklist.xlsx` â† QuÃ© hace VIT

- **Recursos/**: PolÃ­ticas ISO examples, control mapping

---

## âœ… ESTADO ACTUAL (4 marzo 2026)

**Sprint 1 COMPLETADO** âœ…
- âœ… AuditLog model + signals (implementado, probado, funcional)
- âœ… Migraciones (todas aplicadas, DB consistente)
- âœ… ProjectUser serializers + viewsets (CRUD completo, filtrado por rol)
- âœ… Test data (backend/scripts/populate_demo_data.py crea datos de prueba realistas)
- âœ… Demo automatizado (backend/tests/03_demo_sprint/test_demo_sprint1.py valida todos los escenarios)
- âœ… Git: Commit v0.1-sprint1 taggeado, historial limpio

**ValidaciÃ³n**: Todos los 7 endpoints protegidos, 3 roles funcionando, AuditLog registrando cambios automÃ¡ticamente.

## ðŸ“‹ SIGUIENTES PASOS (SPRINT 2)

### **Sprint 2: PROYECTOS + TAREAS (3-16 marzo)**
1. Crear UI Proyectos (Consultant: crear, ver lista; Admin: ver todas)
2. Auto-generar 5 fases al crear proyecto
3. CRUD Tareas (asignar responsable, cambiar estado, % completado)
4. Dashboard Proyectos (progreso, Ãºltimas tareas, grÃ¡ficas)
5. Validaciones: Solo Consultant puede crear proyectos (permissions + frontend)

### **Frontend (PrÃ³ximo)**
- âœ… Backend listo (API endpoints protegidos)
- â³ Login page conectada a /api/token/
- â³ PrivateRoute (redirigir si sin token)
- â³ Dashboard base (Administrador VIT, Consultor, Cliente - diferentes vistas)
- â³ Proyecto management (crear, listar, editar)

---

## ðŸŽ“ CONCEPTO CLAVE: DUAL RISK SCORING

```
Risk = "Acceso no autorizado a BD"

INHERENT (sin controles):
  Probabilidad: 5 (muy probable)
  Impacto: 5 (catastrÃ³fico)
  Score = 5 Ã— 5 = 25 (CRÃTICO)

SELECCIONAR CONTROLES MITIGANTES:
  A.5.15 (Control de acceso fÃ­sico)
  A.8.24 (EncriptaciÃ³n datos)
  A.6.3 (GestiÃ³n de incidentes)

RESIDUAL (con controles):
  Probabilidad: 2 (poco probable, con encriptaciÃ³n + auditorÃ­a)
  Impacto: 5 (sigue siendo catastrÃ³fico, pero menos probable)
  Score = 2 Ã— 5 = 10 (MODERADO)

EFECTIVIDAD = 25 - 10 = 15 (reducciÃ³n de 60%)
```

**En VIT**: Este cÃ¡lculo debe ser AUTOMÃTICO cuando el Consultant ingresa valores.

---

## ðŸ’¡ INSIGHTS FINALES

1. **VIT es un "Project Management para ISO 27001"** â†’ Fases, tareas, progreso, documentos
2. **El nÃºcleo es Risk Management** â†’ Riesgos inherentes vs residuales, con controles como mitigantes
3. **SoA es la evidencia de cumplimiento** â†’ 93 items del Anexo A, cada uno con estado + evidencia cargada
4. **AuditorÃ­a es CRÃTICA** â†’ Todo cambio debe registrarse (QUIEN/QUE/CUANDO) para auditor externo
5. **Permisos por rol son estrictos** â†’ Admin â‰  Consultant â‰  Client (3 dashboards diferentes)

---

**Archivo completo**: Ver `ANALISIS_REQUIEMIENTOS_ISO27001_VIT.md` (~1900 lÃ­neas) para detalles exhaustivos.

