"""Modelo de datos para Cliente."""


def estructura_cliente():
    """Define la estructura de un documento de cliente en MongoDB."""
    return {
        "nombre": None,
        "email": None,
        "telefono": None,
        "direccion": None,
        "fecha_registro": None,
        "estado": "activo"
    }
