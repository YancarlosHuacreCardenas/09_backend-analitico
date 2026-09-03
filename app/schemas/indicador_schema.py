"""Schema para validar indicadores analíticos."""


def schema_indicador(indicador, valor, unidad="unidades"):
    """Estructura estándar para un indicador/KPI."""
    return {
        "indicador": indicador,
        "valor": valor,
        "unidad": unidad
    }


def schema_respuesta_indicadores(indicadores):
    """Estructura de respuesta con múltiples indicadores."""
    return {
        "estado": "éxito",
        "total_indicadores": len(indicadores),
        "indicadores": indicadores
    }
