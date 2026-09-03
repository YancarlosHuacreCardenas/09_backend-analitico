"""Modelo de datos para Producto."""


def estructura_producto():
    """Define la estructura de un documento de producto en MongoDB."""
    return {
        "nombre": None,
        "categoria": None,
        "precio": 0.0,
        "stock": 0,
        "descripcion": None,
        "estado": "disponible"
    }
