# Examen 2 - Frontend Productos

Frontend desarrollado con React, TypeScript, Vite y Tailwind CSS para la gestión de productos.

## Tecnologías utilizadas

- React
- TypeScript
- Vite
- Tailwind CSS

## Funcionalidades

- Listado de productos
- Alta de productos
- Edición de productos
- Eliminación de productos
- Selección de unidad de medida
- Validación de nombres duplicados
- Estados de carga
- Estado vacío
- Manejo básico de errores

## Requisitos

- Node.js 18 o superior
- npm

## Instalación

Instalar dependencias:

```bash
npm install
```

## Ejecución

Iniciar el servidor de desarrollo:

```bash
npm run dev
```

La aplicación estará disponible en:

```text
http://localhost:5173
```

## Backend requerido

La API debe estar ejecutándose en:

```text
http://127.0.0.1:8000
```

Endpoints utilizados:

```text
GET    /api/v1/productos
POST   /api/v1/productos
PUT    /api/v1/productos/{id}
DELETE /api/v1/productos/{id}

GET    /api/v1/unidades-medida
```

## Estructura del proyecto

```text
src/
 ├─ components/
 │   ├─ Navbar.tsx
 │   ├─ ProductoCard.tsx
 │   ├─ ProductoList.tsx
 │   └─ ProductoModal.tsx
 │
 ├─ types/
 │   ├─ producto.ts
 │   ├─ categoria.ts
 │   └─ unidadMedida.ts
 │
 ├─ App.tsx
 └─ main.tsx
```

## Autor

Gabriel Carbajal