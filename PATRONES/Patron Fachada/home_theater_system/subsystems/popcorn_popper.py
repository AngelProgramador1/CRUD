"""
Subsistema: Máquina de Palomitas
Controla la preparación de palomitas
"""

class PopcornPopper:
    """Máquina automática de palomitas"""
    
    def __init__(self):
        self.is_on = False
        self.is_popping = False
    
    def on(self):
        self.is_on = True
        print("🍿 Máquina de palomitas encendida")
    
    def off(self):
        self.is_on = False
        self.is_popping = False
        print("🍿 Máquina de palomitas apagada")
    
    def pop(self):
        if self.is_on:
            self.is_popping = True
            print("🍿 Haciendo palomitas...")
            print("🍿 ¡Palomitas listas para disfrutar!")
            self.is_popping = False
        else:
            print("🍿 Error: La máquina está apagada")