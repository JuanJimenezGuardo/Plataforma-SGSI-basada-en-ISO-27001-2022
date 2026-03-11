# Tests de Demo y Validacion Funcional (Sprint)

Esta carpeta contiene scripts de validacion funcional usados como evidencia de sprint.

## Proposito

- Validar flujos de negocio completos (demo) con salida legible para presentacion.
- Probar escenarios funcionales puntuales fuera de la suite unitaria/formal.

## Importante

- Estos archivos NO forman parte de la suite formal de pruebas automatizadas.
- La suite formal vive en `backend/apps/*/tests/`.

## Suite Formal (CI / calidad tecnica)

Ejecutar desde `backend/`:

```bash
python manage.py test apps.users.tests apps.companies.tests apps.projects.tests apps.phases.tests apps.tasks.tests
```

## Scripts de Demo

Ejecutar desde `backend/`:

```bash
python tests_demo/test_demo_sprint1.py
python tests_demo/test_permissions.py
python tests_demo/test_endpoints.py
python tests_demo/test_auditlog.py
python tests_demo/test_auditlog_endpoint.py
python tests_demo/test_project_user.py
python tests_demo/test_signals.py
python tests_demo/test_backend.py
```

## Recomendacion para sustentacion

- Mostrar resultados de la suite formal por separado.
- Mostrar scripts demo como evidencia funcional del sprint.
