"""Rutas API para Ventas."""

from flask import Blueprint

ventas_bp = Blueprint("ventas", __name__, url_prefix="/api/ventas")


@ventas_bp.route("/", methods=["GET"])
def listar_ventas():
    """Endpoint para obtener todas las ventas."""
    return {"mensaje": "Listado de ventas - Endpoint en construcción"}
