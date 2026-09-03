"""Rutas API para Clientes."""

from flask import Blueprint

clientes_bp = Blueprint("clientes", __name__, url_prefix="/api/clientes")


@clientes_bp.route("/", methods=["GET"])
def listar_clientes():
    """Endpoint para obtener todos los clientes."""
    return {"mensaje": "Listado de clientes - Endpoint en construcción"}
