"""Servicio de lógica de negocio para Productos."""

from app.repositories.producto_repository import ProductoRepository


class ProductosService:
    """Contiene la lógica de negocio para el procesamiento de productos."""

    def __init__(self):
        self.repositorio = ProductoRepository()

    def listar_productos(self):
        """Obtiene todos los productos."""
        return self.repositorio.obtener_todos()

    def obtener_producto(self, producto_id):
        """Obtiene un producto por ID."""
        return self.repositorio.obtener_por_id(producto_id)

    def crear_producto(self, datos):
        """Crea un nuevo producto."""
        return self.repositorio.insertar(datos)

    def actualizar_producto(self, producto_id, datos):
        """Actualiza un producto existente."""
        return self.repositorio.actualizar(producto_id, datos)

    def eliminar_producto(self, producto_id):
        """Elimina un producto."""
        return self.repositorio.eliminar(producto_id)
