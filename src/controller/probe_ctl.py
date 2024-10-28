class ProbeController:    
    
    async def health(self):
        return {
            "status_code": 200,
            "uri": "/health",
            "status": "UP"
        }

    async def ready(self):
        return {
            "status_code": 200,
            "uri": "/ready",
            "status": "UP"
        }