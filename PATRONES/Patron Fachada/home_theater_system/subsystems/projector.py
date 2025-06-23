"""
Subsistema: Proyector
Maneja la proyección de video y configuraciones de imagen
"""

class Projector:
    """Proyector con múltiples modos de visualización"""
    
    def __init__(self):
        self.is_on = False
        self.input_source = None
        self.display_mode = "Standard"
    
    def on(self):
        self.is_on = True
        print("📽️ Proyector encendido")
    
    def off(self):
        self.is_on = False
        print("📽️ Proyector apagado")
    
    def set_input(self, source: str):
        self.input_source = source
        print(f"📽️ Proyector configurado para entrada: {source}")
    
    def wide_screen_mode(self):
        self.display_mode = "Wide Screen"
        print("📽️ Modo pantalla ancha activado")
    
    def standard_mode(self):
        self.display_mode = "Standard"
        print("📽️ Modo estándar activado")