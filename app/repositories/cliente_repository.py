"""Repositorio para operaciones con la colección de clientes en MongoDB."""

from app.database.mongodb import obtener_db


class ClienteRepository:
    """Gestiona consultas y operaciones con la colección clientes."""

    def __init__(self):
        self.coleccion = obtener_db()["clientes"]

    def obtener_todos(self):
        """Retorna todos los clientes."""
        return list(self.coleccion.find({}, {"_id": 0}))

    def obtener_por_id(self, cliente_id):
        """Retorna un cliente por su ID."""
        return self.coleccion.find_one({"_id": cliente_id})

    def insertar(self, cliente):
        """Inserta un nuevo cliente."""
        resultado = self.coleccion.insert_one(cliente)
        return str(resultado.inserted_id)

    def actualizar(self, cliente_id, datos):
        """Actualiza un cliente existente."""
        return self.coleccion.update_one({"_id": cliente_id}, {"$set": datos})

    def eliminar(self, cliente_id):
        """Elimina un cliente por su ID."""
        return self.coleccion.delete_one({"_id": cliente_id})
