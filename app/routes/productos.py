"""Rutas API para Productos."""

from flask import Blueprint

productos_bp = Blueprint("productos", __name__, url_prefix="/api/productos")


@productos_bp.route("/", methods=["GET"])
def listar_productos():
    """Endpoint para obtener todos los productos."""
    return {"mensaje": "Listado de productos - Endpoint en construcción"}
