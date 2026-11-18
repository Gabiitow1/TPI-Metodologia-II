# Food Store API

## Requisitos

- Python 3.14+
- PostgreSQL

## Instalación

```bash
python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt
```

## Variables de entorno

Crear archivo `.env`:

```env
DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/foodstore
```

## Ejecución

```bash
fastapi dev app/main.py
```

## Documentación

http://127.0.0.1:8000/docs