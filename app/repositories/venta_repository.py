"""Repositorio para operaciones con la colección de ventas en MongoDB."""

from app.database.mongodb import obtener_db


class VentaRepository:
    """Gestiona consultas y operaciones con la colección ventas."""

    def __init__(self):
        self.coleccion = obtener_db()["ventas"]

    def obtener_todas(self):
        """Retorna todas las ventas."""
        return list(self.coleccion.find({}, {"_id": 0}))

    def obtener_por_id(self, venta_id):
        """Retorna una venta por su ID."""
        return self.coleccion.find_one({"_id": venta_id})

    def insertar(self, venta):
        """Inserta una nueva venta."""
        resultado = self.coleccion.insert_one(venta)
        return str(resultado.inserted_id)

    def actualizar(self, venta_id, datos):
        """Actualiza una venta existente."""
        return self.coleccion.update_one({"_id": venta_id}, {"$set": datos})

    def eliminar(self, venta_id):
        """Elimina una venta por su ID."""
        return self.coleccion.delete_one({"_id": venta_id})
