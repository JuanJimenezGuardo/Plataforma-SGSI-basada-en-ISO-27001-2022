# Estructura de Pruebas VIT

Para evitar confusiones, las pruebas están divididas en dos grandes grupos: formales y demo.

## A. Pruebas Formales (Revisión CI/Arquitectura)

Son las que se ejecutan automáticamente para garantizar la integridad completa.

1. **Unitarias por App (`backend/apps/*/tests/`)**
   Contienen las pruebas atómicas para cada componente (models, endpoints).
   ```bash
   python manage.py test apps.users.tests apps.companies.tests apps.projects.tests apps.phases.tests apps.tasks.tests
   ```

2. **Integración / Smoke (`backend/tests/00_smoke/`, `backend/tests/01_permisos_roles/`)**
   Agrupan pruebas trasversales automatizadas con `TestCase`.
   ```bash
   python manage.py test tests.01_permisos_roles.test_permissions
   ```

## B. Pruebas Demo (Sustentación de Sprint)

Son scripts Python planos escritos explícitamente para mostrar flujo funcional a negocio.
Imprimen paso a paso en consola con colores para sustentación guiada.

1. **Auditoría visual (`backend/tests/02_auditoria/`)**
   ```bash
   python backend/tests/02_auditoria/test_auditlog.py
   ```

2. **Flujo completo Sprint (`backend/tests/03_demo_sprint/`)**
   ```bash
   python backend/tests/03_demo_sprint/test_demo_sprint1.py
   ```
