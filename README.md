# TPI - Metodología de Sistemas II

## Evolución profesional de un sistema existente: calidad, deuda técnica, refactoring y revisión técnica

### Alumno
Gabriel Carbajal

### Comisión
15

### Docente
Oscar Londero

---

# Descripción del Proyecto

Este proyecto fue desarrollado como base para el Trabajo Práctico Integrador de la asignatura Metodología de Sistemas II.

Consiste en un sistema de gestión de productos implementado mediante una arquitectura cliente-servidor, compuesto por un backend desarrollado con FastAPI y un frontend desarrollado con React y TypeScript.

El trabajo se enfoca en el análisis de calidad interna y externa del software, identificación de deuda técnica, detección de code smells, aplicación de principios SOLID, buenas prácticas de Clean Code, refactoring seguro y revisión técnica profesional.

---

# Funcionalidades Principales

- Alta de productos.
- Consulta de productos.
- Modificación de productos.
- Baja lógica de productos.
- Gestión de categorías.
- Gestión de unidades de medida.
- Asociación entre productos y categorías.
- Búsqueda y filtrado de productos.
- Persistencia de datos mediante base de datos PostgreSQL.
- Documentación automática mediante Swagger.

---

# Arquitectura del Sistema

## Backend

El backend se encuentra dividido en módulos independientes:

- Producto
- Categoría
- Unidad de Medida
- Producto Categoría
- Core

Cada módulo implementa:

- model.py
- schema.py
- service.py
- router.py

## Frontend

El frontend se encuentra desarrollado mediante componentes reutilizables:

- ProductoCard
- ProductoList
- ProductoModal
- CategoriaCard
- CategoriaList
- CategoriaModal
- Navbar

---

# Tecnologías Utilizadas

## Backend

- Python
- FastAPI
- SQLModel
- PostgreSQL
- Pydantic
- SQLAlchemy

## Frontend

- React
- TypeScript
- Vite
- CSS

## Herramientas

- Git
- GitHub
- Swagger UI
- Visual Studio Code

---

# Estructura del Repositorio

```text
TPI-Metodologia-II
│
├── docs
│   ├── checklist-code-review.md
│   ├── code-smells.md
│   └── evidencias.md
│
├── examen_2_backend
│
└── examen_2_categorias
```

# Instalación

## Backend

Ingresar al directorio:

```bash
cd examen_2_backend
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar servidor:

```bash
python -m fastapi dev app/main.py
```

Documentación Swagger:

```text
http://127.0.0.1:8000/docs
```

---

## Frontend

Ingresar al directorio:

```bash
cd examen_2_categorias
```

Instalar dependencias:

```bash
npm install
```

Ejecutar aplicación:

```bash
npm run dev
```

---

# Evidencias de Calidad

Durante el desarrollo del TPI se realizaron las siguientes actividades:

- Análisis de calidad externa e interna.
- Identificación de deuda técnica.
- Detección de 8 code smells.
- Aplicación de principios SOLID.
- Aplicación de prácticas Clean Code.
- Documentación de refactorings.
- Ejecución de pruebas funcionales.
- Revisión técnica mediante checklist de code review.
- Control de versiones mediante Git y GitHub.

---

# Tags del Proyecto

Para asegurar la trazabilidad del trabajo se utilizaron los siguientes tags:

- estado-inicial
- etapa-diagnostico
- etapa-refactoring
- etapa-pruebas
- etapa-docs
- estado-refactorizado

---

# Uso de Inteligencia Artificial

Se utilizó Microsoft Copilot como herramienta de asistencia para:

- Comprensión de conceptos.
- Identificación de oportunidades de refactoring.
- Revisión de alternativas de diseño.
- Redacción y organización de documentación técnica.

La implementación, validación y defensa del trabajo corresponden íntegramente al autor.

---

# Autor

Gabriel Carbajal

Trabajo Práctico Integrador - Metodología de Sistemas II

Universidad Tecnológica Nacional
