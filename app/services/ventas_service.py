"""Servicio de lógica de negocio para Ventas."""

from app.repositories.venta_repository import VentaRepository


class VentasService:
    """Contiene la lógica de negocio para el procesamiento de ventas."""

    def __init__(self):
        self.repositorio = VentaRepository()

    def listar_ventas(self):
        """Obtiene todas las ventas."""
        return self.repositorio.obtener_todas()

    def obtener_venta(self, venta_id):
        """Obtiene una venta por ID."""
        return self.repositorio.obtener_por_id(venta_id)

    def crear_venta(self, datos):
        """Crea una nueva venta."""
        datos["total"] = datos.get("cantidad", 0) * datos.get("precio_unitario", 0)
        return self.repositorio.insertar(datos)

    def actualizar_venta(self, venta_id, datos):
        """Actualiza una venta existente."""
        return self.repositorio.actualizar(venta_id, datos)

    def eliminar_venta(self, venta_id):
        """Elimina una venta."""
        return self.repositorio.eliminar(venta_id)
