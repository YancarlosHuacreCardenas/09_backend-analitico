"""Servicio de análisis y cálculo de indicadores (KPIs)."""

from app.repositories.venta_repository import VentaRepository


class AnalyticsService:
    """Contiene la lógica para cálculo de indicadores analíticos."""

    def __init__(self):
        self.venta_repo = VentaRepository()

    def total_ventas(self):
        """Calcula el total de ventas registradas."""
        ventas = self.venta_repo.obtener_todas()
        return {
            "indicador": "Total de Ventas",
            "valor": len(ventas)
        }

    def ingresos_totales(self):
        """Calcula los ingresos totales."""
        ventas = self.venta_repo.obtener_todas()
        total = sum(v.get("total", 0) for v in ventas)
        return {
            "indicador": "Ingresos Totales",
            "valor": total
        }

    def ticket_promedio(self):
        """Calcula el ticket promedio por venta."""
        ventas = self.venta_repo.obtener_todas()
        if not ventas:
            return {"indicador": "Ticket Promedio", "valor": 0}
        total = sum(v.get("total", 0) for v in ventas)
        promedio = total / len(ventas)
        return {
            "indicador": "Ticket Promedio",
            "valor": round(promedio, 2)
        }
