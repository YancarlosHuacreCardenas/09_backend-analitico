"""Repositorio para operaciones con la colección de productos en MongoDB."""

from app.database.mongodb import obtener_db


class ProductoRepository:
    """Gestiona consultas y operaciones con la colección productos."""

    def __init__(self):
        self.coleccion = obtener_db()["productos"]

    def obtener_todos(self):
        """Retorna todos los productos."""
        return list(self.coleccion.find({}, {"_id": 0}))

    def obtener_por_id(self, producto_id):
        """Retorna un producto por su ID."""
        return self.coleccion.find_one({"_id": producto_id})

    def insertar(self, producto):
        """Inserta un nuevo producto."""
        resultado = self.coleccion.insert_one(producto)
        return str(resultado.inserted_id)

    def actualizar(self, producto_id, datos):
        """Actualiza un producto existente."""
        return self.coleccion.update_one({"_id": producto_id}, {"$set": datos})

    def eliminar(self, producto_id):
        """Elimina un producto por su ID."""
        return self.coleccion.delete_one({"_id": producto_id})
