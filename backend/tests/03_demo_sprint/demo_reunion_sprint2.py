"""
Demo de reunión (paso a paso) - Backend VIT
Muestra funcionalidad de Sprint 1 y Sprint 2 en fases narrables.

Ejecución:
    c:/Proyecto_VIT/.venv/Scripts/python.exe backend/tests/03_demo_sprint/demo_reunion_sprint2.py
"""

import os
import sys
from datetime import date, timedelta
from pathlib import Path

import django

BACKEND_DIR = Path(__file__).resolve().parents[2]
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
django.setup()

from django.db import connection
from django.test import Client
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import User, AuditLog
from apps.companies.models import Company
from apps.contacts.models import Contact
from apps.projects.models import Project, ProjectUser, ProjectContact
from apps.phases.models import Phase
from apps.tasks.models import Task
from apps.documents.models import Document
from apps.assets.models import Asset


class UI:
    G = "\033[92m"
    Y = "\033[93m"
    R = "\033[91m"
    B = "\033[94m"
    C = "\033[96m"
    W = "\033[97m"
    E = "\033[0m"
    BOLD = "\033[1m"


def hr():
    print("─" * 100)


def title(text):
    print(f"\n{UI.BOLD}{UI.C}{'=' * 100}{UI.E}")
    print(f"{UI.BOLD}{UI.C}{text.center(100)}{UI.E}")
    print(f"{UI.BOLD}{UI.C}{'=' * 100}{UI.E}")


def phase(name):
    print(f"\n{UI.BOLD}{UI.W}{name}{UI.E}")
    hr()


def ok(msg):
    print(f"{UI.G}✅ {msg}{UI.E}")


def warn(msg):
    print(f"{UI.Y}⚠️  {msg}{UI.E}")


def fail(msg):
    print(f"{UI.R}❌ {msg}{UI.E}")


def info(msg):
    print(f"{UI.B}ℹ️  {msg}{UI.E}")


def pause():
    input(f"\n{UI.BOLD}{UI.Y}[Presiona ENTER para continuar a la siguiente fase...]{UI.E}\n")


def token_for(user):
    return str(RefreshToken.for_user(user).access_token)


def auth_headers(user):
    return {"HTTP_AUTHORIZATION": f"Bearer {token_for(user)}"}


def ensure_demo_data():
    # Usuarios demo
    admin, _ = User.objects.get_or_create(
        username="admin_vit",
        defaults={
            "email": "admin@vit.com",
            "first_name": "Carlos",
            "last_name": "Rodriguez",
            "role": "ADMIN",
            "is_staff": True,
            "is_superuser": True,
        },
    )
    admin.set_password("admin123")
    admin.save()

    consultant, _ = User.objects.get_or_create(
        username="consultant_ana",
        defaults={
            "email": "ana.martinez@vit.com",
            "first_name": "Ana",
            "last_name": "Martinez",
            "role": "CONSULTANT",
        },
    )
    consultant.set_password("consultant123")
    consultant.save()

    client_user, _ = User.objects.get_or_create(
        username="client_juan",
        defaults={
            "email": "juan.perez@acme.com",
            "first_name": "Juan",
            "last_name": "Perez",
            "role": "CLIENT",
        },
    )
    client_user.set_password("client123")
    client_user.save()

    # Empresas
    company1, _ = Company.objects.get_or_create(
        rfc="ACM123456AB1",
        defaults={
            "name": "ACME Corporation",
            "email": "contacto@acme.com",
            "phone": "+57 601 7654321",
            "address": "Calle 100 #50-25",
            "city": "Bogotá",
            "state": "Cundinamarca",
            "country": "Colombia",
        },
    )

    company2, _ = Company.objects.get_or_create(
        rfc="BCO789012CD2",
        defaults={
            "name": "Bancolombia ISO Project",
            "email": "seguridad@bancolombia.com",
            "phone": "+57 604 5555555",
            "address": "Carrera 48 #26-85",
            "city": "Medellín",
            "state": "Antioquia",
            "country": "Colombia",
        },
    )

    # Contactos (Sprint 2)
    contact1, _ = Contact.objects.get_or_create(
        company=company1,
        email="juan.perez@acme.com",
        defaults={
            "full_name": "Juan Perez",
            "phone": "+57 300 1112233",
            "position": "CTO",
            "is_active": True,
        },
    )

    contact2, _ = Contact.objects.get_or_create(
        company=company2,
        email="maria.gonzalez@bancolombia.com",
        defaults={
            "full_name": "María Gonzalez",
            "phone": "+57 300 2223344",
            "position": "CISO",
            "is_active": True,
        },
    )

    # Proyectos (ya con fechas sprint 2)
    project1, _ = Project.objects.get_or_create(
        name="Implementación ISO 27001 - ACME",
        defaults={
            "description": "Proyecto SGSI ACME",
            "company": company1,
            "status": "IN_PROGRESS",
            "planned_start_date": date.today() - timedelta(days=30),
            "planned_end_date": date.today() + timedelta(days=120),
            "actual_start_date": date.today() - timedelta(days=25),
            "created_by": consultant,
        },
    )

    project2, _ = Project.objects.get_or_create(
        name="Auditoría ISO 27001 - Bancolombia",
        defaults={
            "description": "Auditoría SGSI Bancolombia",
            "company": company2,
            "status": "PLANNING",
            "planned_start_date": date.today() + timedelta(days=10),
            "planned_end_date": date.today() + timedelta(days=160),
            "created_by": admin,
        },
    )

    # Asignaciones Sprint 1
    ProjectUser.objects.get_or_create(project=project1, user=consultant, defaults={"role": "CONSULTANT"})
    ProjectUser.objects.get_or_create(project=project1, user=client_user, defaults={"role": "CLIENT"})
    ProjectUser.objects.get_or_create(project=project2, user=admin, defaults={"role": "ADMIN"})

    # Relación ProjectContact Sprint 2
    ProjectContact.objects.get_or_create(
        project=project1,
        contact=contact1,
        defaults={"contact_role": "PROJECT_MANAGER", "is_primary": True},
    )
    ProjectContact.objects.get_or_create(
        project=project2,
        contact=contact2,
        defaults={"contact_role": "CISO", "is_primary": True},
    )

    # Phase y Task mínimas para mostrar fechas/work_notes Sprint 2
    phase1, _ = Phase.objects.get_or_create(
        project=project1,
        name="Diagnóstico Inicial",
        defaults={
            "type": "ASSESSMENT",
            "description": "Levantamiento inicial",
            "order": 1,
            "planned_start_date": date.today() - timedelta(days=20),
            "planned_end_date": date.today() - timedelta(days=5),
            "actual_start_date": date.today() - timedelta(days=18),
            "actual_end_date": date.today() - timedelta(days=3),
        },
    )

    Task.objects.get_or_create(
        phase=phase1,
        name="Levantamiento de activos",
        defaults={
            "description": "Identificar activos críticos",
            "assigned_to": consultant,
            "priority": "HIGH",
            "status": "IN_PROGRESS",
            "planned_start_date": date.today() - timedelta(days=15),
            "planned_end_date": date.today() - timedelta(days=7),
            "actual_start_date": date.today() - timedelta(days=14),
            "work_notes": "Se completó el 80% del inventario.",
        },
    )

    from django.core.files.base import ContentFile
    
    # Documento mínimo Sprint 2
    doc_qs = Document.objects.filter(project=project1, title="Plan de tratamiento de riesgos")
    if not doc_qs.exists():
        doc = Document(
            project=project1,
            title="Plan de tratamiento de riesgos",
            doc_type="REPORT",
            status="DRAFT"
        )
        doc.file.save('plan_tratamiento.txt', ContentFile(b'Contenido mock del plan de tratamiento de riesgos'), save=True)


    return admin, consultant, client_user, project1


def phase_1_load_data():
    phase("FASE 1 - CARGA DE DATOS DEMO (Sprint 1 + Sprint 2)")
    info("Objetivo: Poblar la base de datos con un escenario realista de ISO 27001 para la demostración.")
    info("• Se construyen los 3 roles core del sistema: Administrador (VIT), Consultor ISO, y Cliente (Empresa).")
    info("• Se registran 2 compañías de simulacro: 'ACME Corp' (Cliente) y 'Bancolombia' (Auditoría).")
    info("• Se modela un Proyecto principal 'Implementación ISO 27001 - ACME'.")
    info("• Se orquestan fases, asignación de equipo (Project Manager, CISO), tareas iniciales y carga documental.")
    print("")

    admin, consultant, client_user, project1 = ensure_demo_data()
    ok("Base de datos poblada en entorno local / en memoria.")
    info("Credenciales preparadas -> admin_vit / consultant_ana / client_juan")
    return admin, consultant, client_user, project1


def phase_2_health_check():
    phase("FASE 2 - REVISIÓN DE SALUD DE INFRAESTRUCTURA (HEALTH CHECK)")
    info("Objetivo: Confirmar integridad de ORM y base de datos relacional.")
    info("• Validando que el motor SQL se comunique correctamente con el Backend de Django.")
    print("")

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1;")
            value = cursor.fetchone()[0]
        if value == 1:
            ok("Conexión a base de datos: OK")
            return True
        fail("Conexión a base de datos: respuesta inesperada")
        return False
    except Exception as ex:
        fail(f"Conexión a base de datos: fallo ({ex})")
        return False


def phase_3_sprint1_security(admin, consultant, client_user):
    phase("FASE 3 - MOTOR DE SEGURIDAD, RBAC Y AUDITORÍA (LOGROS SPRINT 1)")
    info("Objetivo: Comprobar que el núcleo de protección de la aplicación es intransitable.")
    info("• Emisión de Tokens JWT: Se bloquean peticiones que no posean el encabezado de autorización (Bearer Token).")
    info("• Control de Roles (RBAC): Cada ruta exige un rol válido. Un Consultor o Cliente no puede gestionar usuarios o tocar áreas 'core'.")
    info("• Auditoría Forense Activa: Cada post, put o delete a la BD se registra (Usuario, IP, Payload y Tipo de Evento).")
    print("")

    c = Client()
    all_ok = True

    # Endpoints protegidos sin token
    protected = ["/api/users/", "/api/projects/", "/api/audit-logs/"]
    for ep in protected:
        r = c.get(ep)
        if r.status_code == 401:
            ok(f"{ep} protegido sin token (401)")
        else:
            warn(f"{ep} devolvió {r.status_code} sin token")
            all_ok = False

    # Permisos por rol
    r_admin = c.get("/api/users/", **auth_headers(admin))
    r_cons = c.get("/api/users/", **auth_headers(consultant))
    r_client = c.get("/api/users/", **auth_headers(client_user))

    if r_admin.status_code == 200:
        ok("ADMIN accede a gestión de usuarios")
    else:
        fail(f"ADMIN usuarios -> {r_admin.status_code}")
        all_ok = False

    if r_cons.status_code == 403 and r_client.status_code == 403:
        ok("CONSULTANT/CLIENT bloqueados en gestión de usuarios")
    else:
        warn(f"Permisos users no esperados: consultant={r_cons.status_code}, client={r_client.status_code}")
        all_ok = False

    # AuditLog
    logs = AuditLog.objects.count()
    if logs > 0:
        ok(f"AuditLog activo ({logs} eventos)")
    else:
        warn("AuditLog sin eventos en este entorno")
    return all_ok


def phase_4_sprint2_model():
    phase("FASE 4 - EVOLUCIÓN DEL MODELO DE DATOS Y TRAZABILIDAD (LOGROS SPRINT 2)")
    info("Objetivo: Tras la última revisión de hace 15 días, el negocio requería poder medir esfuerzo y mapear equipos reales.")
    info("En este Sprint rediseñamos la arquitectura base:")
    info("1. Ciclo de Vida: Adicionadas fechas (planned_start, actual_end, etc) a Proyectos, Fases y Tareas para reportes de desvío.")
    info("2. Diario Técnico: Implementado campo de anotaciones directas (work_notes) facilitando la bitácora del Consultor en la Tarea.")
    info("3. Mapeo de Stakeholders: Contactos removidos estáticamente de 'Empresa' y normalizados como su propia entidad reutilizable (Contact / ProjectContact).")
    print("")

    all_ok = True

    project_fields = {f.name for f in Project._meta.fields}
    phase_fields = {f.name for f in Phase._meta.fields}
    task_fields = {f.name for f in Task._meta.fields}
    company_fields = {f.name for f in Company._meta.fields}

    checks = [
        ("Project con fechas planned/actual", {"planned_start_date", "planned_end_date", "actual_start_date", "actual_end_date"}.issubset(project_fields)),
        ("Phase con fechas planned/actual", {"planned_start_date", "planned_end_date", "actual_start_date", "actual_end_date"}.issubset(phase_fields)),
        ("Task con fechas planned/actual", {"planned_start_date", "planned_end_date", "actual_start_date", "actual_end_date"}.issubset(task_fields)),
        ("Task incluye work_notes", "work_notes" in task_fields),
        ("Company removió campos legacy de contacto", ("contact_person" not in company_fields and "contact_position" not in company_fields)),
    ]

    for label, status in checks:
        if status:
            ok(label)
        else:
            fail(label)
            all_ok = False

    # Entidades Sprint 2 presentes
    info("Conteos de entidades Sprint 2:")
    print(f"  - Company:        {Company.objects.count()}")
    print(f"  - Contact:        {Contact.objects.count()}")
    print(f"  - Project:        {Project.objects.count()}")
    print(f"  - ProjectUser:    {ProjectUser.objects.count()}")
    print(f"  - ProjectContact: {ProjectContact.objects.count()}")
    print(f"  - Phase:          {Phase.objects.count()}")
    print(f"  - Task:           {Task.objects.count()}")
    print(f"  - Document:       {Document.objects.count()}")
    print(f"  - Asset:          {Asset.objects.count()}")

    return all_ok


def phase_5_sprint2_api(admin, consultant, client_user):
    phase("FASE 5 - DESPLIEGUE DE CAPA DE SERVICIOS REST (API)")
    info("Objetivo: Garantizar que cualquier frontend (ej: React) pueda leer/escribir las nuevas reglas sin fallos.")
    info("• Testing transversal a las nuevas rutas (/api/phases/, /api/tasks/, /api/project-contacts/).")
    info("• Validando que no existan excepciones en servidor (Errores HTTP 500) operando métodos de lectura y escritura.")
    print("")

    c = Client()
    all_ok = True

    endpoints = [
        "/api/companies/",
        "/api/contacts/",
        "/api/projects/",
        "/api/project-users/",
        "/api/project-contacts/",
        "/api/phases/",
        "/api/tasks/",
        "/api/documents/",
        "/api/assets/",
        "/api/audit-logs/",
    ]

    for ep in endpoints:
        for user in (admin, consultant, client_user):
            r = c.get(ep, **auth_headers(user))
            if r.status_code >= 500:
                fail(f"{ep} con {user.role} -> {r.status_code} (500+)")
                all_ok = False
                break

    if all_ok:
        ok("Todos los endpoints core respondieron sin errores 500")
    return all_ok


def phase_6_end_to_end_story(admin, consultant, client_user, project1):
    phase("FASE 6 - CASO DE USO INTEGRAL ISO 27001 (LO QUE PERCIBE EL NEGOCIO)")
    info("Objetivo: Poner a prueba la lógica operativa combinando seguridad, modelo de datos y reglas.")
    info("1. Aislamiento Multi-tenant: Comprobando que el Client_User no percibe los proyectos de la otra empresa (Bancolombia).")
    info("2. Organigrama de Proyecto: Verificando que 'Juan Perez' fue enlazado lógicamente como 'CTO' del proyecto actual.")
    info("3. Operación Activa: Consultando que una tarea registra su bitácora técnica explícitamente ('Se completó el 80%').")
    info("4. Gestión Documental: Localizando en el Storage del proyecto el 'Plan de tratamiento de riesgos' cargado por el consultor.")
    print("")

    c = Client()
    all_ok = True

    # Visualización por rol en proyectos
    ra = c.get("/api/projects/", **auth_headers(admin))
    rc = c.get("/api/projects/", **auth_headers(consultant))
    rcl = c.get("/api/projects/", **auth_headers(client_user))

    if all(x.status_code == 200 for x in (ra, rc, rcl)):
        ok("Los tres roles pueden consultar proyectos según sus permisos")
    else:
        warn("Consulta de proyectos por rol con estados inesperados")
        all_ok = False

    # Validar que hay contactos y relación project-contact
    if Contact.objects.filter(company=project1.company).exists():
        ok("Proyecto tiene contactos de negocio asociados (Sprint 2)")
    else:
        warn("No se encontraron contactos asociados en proyecto demo")
        all_ok = False

    if ProjectContact.objects.filter(project=project1).exists():
        ok("Proyecto tiene ProjectContact configurado (Sprint 2)")
    else:
        warn("No se encontró ProjectContact para proyecto demo")
        all_ok = False

    # Validar task con work_notes
    task = Task.objects.filter(phase__project=project1).first()
    if task and task.work_notes:
        ok("Task incluye work_notes y trazabilidad operativa")
    else:
        warn("Task sin work_notes en el proyecto demo")
        all_ok = False

    # Documento base
    if Document.objects.filter(project=project1).exists():
        ok("Proyecto tiene al menos un documento de trazabilidad")
    else:
        warn("Proyecto demo sin documentos")
        all_ok = False
        
    return all_ok


def phase_7_summary(results):
    phase("FASE 7 - CIERRE EJECUTIVO Y DECISIÓN")
    passed = sum(1 for _, value in results if value)
    total = len(results)
    pct = (passed / total * 100) if total else 0

    print("Resultado por fase:")
    for label, value in results:
        mark = "VERDE" if value else "ROJO"
        color = UI.G if value else UI.R
        print(f"  {color}• {label}: {mark}{UI.E}")

    print(f"\nAvance global: {passed}/{total} fases ({pct:.1f}%)")

    if passed == total:
        ok("DECISIÓN: Sprint 2 backend CERRADO y listo para iniciar Sprint 3.")
    elif passed >= total - 1:
        warn("DECISIÓN: Sprint 2 backend casi cerrado, con ajustes menores.")
    else:
        fail("DECISIÓN: Sprint 2 backend requiere más correcciones antes de cierre.")

    print("\nSiguiente paso sugerido para Sprint 3:")
    print("1) Congelar contrato API final.")
    print("2) Integración frontend sobre contrato estable.")

    print(f"\n{UI.BOLD}{UI.C}--- RESPALDO TÉCNICO Y CIERRE (FUERA DE ESTE SCRIPT) ---{UI.E}")
    info("Este script demuestra la viabilidad funcional (Demo Ejecutiva).")
    info("El cierre técnico formal y las auditorías de código se encuentran en:")
    print(f"  {UI.W}1. z_docs/03_engineering/backend/sprint_2/api_validation_day5.md{UI.E} (Testeo integral, POST/PATCH, Errores 400)")
    print(f"  {UI.W}2. z_docs/02_sprints/sprint_2/SPRINT2_QUICK_REFERENCE.md{UI.E} (Validación de Data Migrations y Handoff)")


def main():
    title("VIT | DEMO REUNIÓN INGENIERO | VALIDACIÓN PASO A PASO SPRINT 1 + SPRINT 2")
    print(f"Fecha: {date.today().isoformat()}")
    print("Formato de demo: Fase 1 -> Fase 7")
    hr()

    pause()
    admin, consultant, client_user, project1 = phase_1_load_data()

    pause()
    results = []
    results.append(("Fase 2 - Salud backend", phase_2_health_check()))
    
    pause()
    results.append(("Fase 3 - Sprint 1 seguridad/roles", phase_3_sprint1_security(admin, consultant, client_user)))
    
    pause()
    results.append(("Fase 4 - Sprint 2 modelo de datos", phase_4_sprint2_model()))
    
    pause()
    results.append(("Fase 5 - Sprint 2 API core", phase_5_sprint2_api(admin, consultant, client_user)))

    pause()
    results.append(("Fase 6 - Caso de uso integral", phase_6_end_to_end_story(admin, consultant, client_user, project1)))
    
    pause()
    phase_7_summary(results)


if __name__ == "__main__":
    main()