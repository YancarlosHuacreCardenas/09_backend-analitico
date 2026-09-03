from pymongo import MongoClient
from app.config.settings import MONGO_URI, MONGO_DB_NAME


client = None
db = None


def conectar_mongodb():
    """Establece la conexión con MongoDB."""
    global client, db
    try:
        client = MongoClient(MONGO_URI)
        db = client[MONGO_DB_NAME]
        print(f"✅ Conexión exitosa a MongoDB: {MONGO_DB_NAME}")
        return db
    except Exception as e:
        print(f"❌ Error al conectar con MongoDB: {e}")
        raise e


def obtener_db():
    """Retorna la instancia de la base de datos."""
    global db
    if db is None:
        conectar_mongodb()
    return db


def cerrar_conexion():
    """Cierra la conexión con MongoDB."""
    global client
    if client:
        client.close()
        print("🔒 Conexión con MongoDB cerrada.")
