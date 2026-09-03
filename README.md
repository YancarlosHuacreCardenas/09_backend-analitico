# 🚀 Backend Analítico

Backend analítico construido con **Flask**, **MongoDB** y arquitectura por capas.

## 📋 Estructura del Proyecto

```
Backend-Analitico/
├── app/
│   ├── config/          # Configuraciones y variables del sistema
│   │   └── settings.py
│   ├── database/        # Conexión con MongoDB
│   │   └── mongodb.py
│   ├── models/          # Estructura de datos
│   │   ├── venta.py
│   │   ├── cliente.py
│   │   └── producto.py
│   ├── repositories/    # Consultas y operaciones con MongoDB
│   │   ├── venta_repository.py
│   │   ├── cliente_repository.py
│   │   └── producto_repository.py
│   ├── services/        # Lógica de negocio e indicadores
│   │   ├── ventas_service.py
│   │   ├── clientes_service.py
│   │   ├── productos_service.py
│   │   └── analytics_service.py
│   ├── routes/          # Endpoints de la API
│   │   ├── ventas.py
│   │   ├── clientes.py
│   │   ├── productos.py
│   │   └── status.py
│   ├── schemas/         # Validación de datos
│   │   └── indicador_schema.py
│   └── main.py          # Punto de entrada
├── tests/
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## 🛠️ Tecnologías

- **Python** - Lenguaje principal
- **Flask** - Framework web
- **MongoDB** - Base de datos NoSQL
- **PyMongo** - Driver de MongoDB para Python

## ⚙️ Instalación

1. Crear entorno virtual:
```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Configurar variables de entorno en `.env`

4. Ejecutar:
```bash
python -m app.main
```

## 🔗 Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/` | Estado de la API |
| GET | `/api/ventas/` | Listado de ventas |
| GET | `/api/clientes/` | Listado de clientes |
| GET | `/api/productos/` | Listado de productos |

## 🏗️ Arquitectura

**Flujo**: Cliente HTTP → Routes → Services → Repositories → MongoDB
