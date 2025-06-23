"""
Subsistema: Pantalla
Controla la pantalla motorizada
"""

class Screen:
    """Pantalla motorizada que sube y baja"""
    
    def __init__(self):
        self.position = "up"  # "up" o "down"
    
    def up(self):
        if self.position == "down":
            self.position = "up"
            print("🎬 Pantalla subiendo...")
            print("🎬 Pantalla guardada")
        else:
            print("🎬 La pantalla ya está guardada")
    
    def down(self):
        if self.position == "up":
            self.position = "down"
            print("🎬 Pantalla bajando...")
            print("🎬 Pantalla desplegada y lista")
        else:
            print("🎬 La pantalla ya está desplegada")