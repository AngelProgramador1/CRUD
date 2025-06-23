"""
Subsistema: Iluminación del Teatro
Controla la iluminación ambiental
"""

class TheaterLights:
    """Sistema de luces con control de intensidad"""
    
    def __init__(self):
        self.brightness = 100  # 0-100%
        self.is_on = True
    
    def on(self):
        self.is_on = True
        self.brightness = 100
        print("💡 Luces encendidas al 100%")
    
    def off(self):
        self.is_on = False
        self.brightness = 0
        print("💡 Luces apagadas")
    
    def dim(self, level: int):
        """Atenúa las luces al nivel especificado (0-100)"""
        if 0 <= level <= 100:
            self.is_on = level > 0
            self.brightness = level
            if level == 0:
                print("💡 Luces apagadas")
            else:
                print(f"💡 Luces atenuadas al {level}%")
        else:
            print("💡 El nivel debe estar entre 0 y 100")