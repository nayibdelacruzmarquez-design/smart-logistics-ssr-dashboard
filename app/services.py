import random

class LogisticaService:
    def get_kpis(self):
        """Simula y calcula los 4 KPIs principales."""
        return {
            "otif": {"titulo": "Tasa OTIF", "valor": f"{random.randint(92, 98)}%", "status": "Óptimo"},
            "server_load": {"titulo": "Carga Servidores", "valor": f"{random.randint(45, 78)}%", "status": "Normal"},
            "inventario": {"titulo": "Items Críticos", "valor": random.randint(12, 25), "status": "Atención"},
            "prediccion": {"titulo": "Predicción Demanda", "valor": "+14.2%", "status": "Crecimiento"}
        }

    def get_stock_critico(self, region: str):
        """Devuelve datos tabulares filtrados para la tabla dinámica."""
        productos_mock = [
            {"sku": "SKU-9921", "nombre": "Sensor Láser Industrial", "zona": "Norte", "stock": 3, "nivel": "Alta"},
            {"sku": "SKU-4412", "nombre": "Servomotor AC 1kW", "zona": "Sur", "stock": 1, "nivel": "Alta"},
            {"sku": "SKU-7723", "nombre": "Controlador Lógico PLC", "zona": "Este", "stock": 5, "nivel": "Media"},
            {"sku": "SKU-1102", "nombre": "Cable Blindado Cat6a", "zona": "Oeste", "stock": 12, "nivel": "Baja"},
            {"sku": "SKU-8834", "nombre": "Actuador Neumático", "zona": "Norte", "stock": 2, "nivel": "Alta"},
        ]
        if region == "Todas":
            return productos_mock
        return [p for p in productos_mock if p["zona"] == region]

    def get_volume_data(self, filtro: str):
        """Simula arrays de datos para representar volumen de envíos."""
        if filtro == "ayer":
            return {"labels": ["08:00", "12:00", "16:00", "20:00"], "valores": [120, 340, 210, 90], "filtro": "Ayer"}
        return {"labels": ["08:00", "12:00", "16:00", "20:00"], "valores": [150, 420, 310, 180], "filtro": "Hoy (Tiempo Real)"}