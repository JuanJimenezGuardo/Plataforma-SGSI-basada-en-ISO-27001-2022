# VIT - Plataforma de Implementacion ISO 27001

Sistema web para gestionar la implementacion de ISO 27001 en empresas. Permite a consultores crear proyectos, evaluar riesgos, gestionar controles y generar documentacion de cumplimiento.

## Tecnologias

**Backend:**
- Django 4.2.8 + Django REST Framework
- PostgreSQL / SQLite
- Python 3.12+

**Frontend:**
- React 18
- Vite
- Axios

## Estructura del Proyecto

```
proyecto_vit/
├── backend/          # API Django REST Framework
│   ├── apps/        # Modulos (users, projects, risks, etc.)
│   ├── config/      # Configuracion Django
│   └── README.md
├── fronted/         # Aplicacion React
│   ├── src/
│   └── package.json
└── architecture/    # Documentacion tecnica
    └── README.md
```

## Configuracion

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # Linux/Mac

pip install -r requirements.txt

# Configurar base de datos en .env
cp .env.example .env

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Correr servidor
python manage.py runserver
```

### Frontend

```bash
cd fronted
npm install
npm run dev
```

El backend corre en `http://localhost:8000`
El frontend corre en `http://localhost:3000`

## Modulos Principales

- **users** - Autenticacion y roles (Admin, Consultor, Cliente)
- **companies** - Gestion de empresas cliente
- **projects** - Proyectos ISO 27001 con fases y tareas
- **risks** - Evaluacion de riesgos (modelo dual inherente/residual)
- **iso_controls** - Catalogo de controles ISO 27001 Anexo A
- **documents** - Gestion de documentos y evidencias
- **reports** - Generacion de reportes de cumplimiento

## API Endpoints

```
POST   /api/users/           # Crear usuario
GET    /api/users/           # Listar usuarios
POST   /api/users/login/     # Login

GET    /api/companies/       # Listar empresas
POST   /api/projects/        # Crear proyecto
GET    /api/risks/           # Listar riesgos
GET    /api/iso-controls/    # Controles ISO
POST   /api/soa-items/       # Statement of Applicability
GET    /api/documents/       # Documentos
POST   /api/evidence/        # Subir evidencia
POST   /api/reports/         # Generar reportes
```

## Documentacion

Ver la carpeta `/architecture` para especificaciones tecnicas:
- Modelo de datos formal
- Arquitectura de gestion de riesgos
- Diccionario de datos
- Cardinalidades y relaciones
- Estrategia de auditoria

## Tests

```bash
cd backend
python manage.py test
```

## Licencia

Proyecto academico - 2026
