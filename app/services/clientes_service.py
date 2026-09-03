"""Servicio de lógica de negocio para Clientes."""

from app.repositories.cliente_repository import ClienteRepository


class ClientesService:
    """Contiene la lógica de negocio para el procesamiento de clientes."""

    def __init__(self):
        self.repositorio = ClienteRepository()

    def listar_clientes(self):
        """Obtiene todos los clientes."""
        return self.repositorio.obtener_todos()

    def obtener_cliente(self, cliente_id):
        """Obtiene un cliente por ID."""
        return self.repositorio.obtener_por_id(cliente_id)

    def crear_cliente(self, datos):
        """Crea un nuevo cliente."""
        return self.repositorio.insertar(datos)

    def actualizar_cliente(self, cliente_id, datos):
        """Actualiza un cliente existente."""
        return self.repositorio.actualizar(cliente_id, datos)

    def eliminar_cliente(self, cliente_id):
        """Elimina un cliente."""
        return self.repositorio.eliminar(cliente_id)
