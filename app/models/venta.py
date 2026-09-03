"""Modelo de datos para Venta."""


def estructura_venta():
    """Define la estructura de un documento de venta en MongoDB."""
    return {
        "fecha": None,
        "cliente_id": None,
        "producto_id": None,
        "cantidad": 0,
        "precio_unitario": 0.0,
        "total": 0.0,
        "metodo_pago": None,
        "estado": "pendiente"
    }
