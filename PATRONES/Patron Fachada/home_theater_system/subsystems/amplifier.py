"""
Subsistema: Amplificador
Maneja la amplificación de audio y configuraciones de sonido
"""

class Amplifier:
    """Amplificador con múltiples configuraciones complejas"""
    
    def __init__(self):
        self.is_on = False
        self.volume = 0
        self.input_source = None
        self.sound_mode = None
    
    def on(self):
        self.is_on = True
        print("🔊 Amplificador encendido")
    
    def off(self):
        self.is_on = False
        self.volume = 0
        print("🔊 Amplificador apagado")
    
    def set_dvd(self):
        self.input_source = "DVD"
        print("🔊 Amplificador configurado para entrada DVD")
    
    def set_cd(self):
        self.input_source = "CD"
        print("🔊 Amplificador configurado para entrada CD")
    
    def set_volume(self, level: int):
        if 0 <= level <= 10:
            self.volume = level
            print(f"🔊 Volumen establecido en {level}")
        else:
            print("🔊 Volumen debe estar entre 0 y 10")
    
    def set_surround_sound(self):
        self.sound_mode = "Surround 5.1"
        print("🔊 Modo de sonido envolvente 5.1 activado")
    
    def set_stereo_sound(self):
        self.sound_mode = "Stereo"
        print("🔊 Modo estéreo activado")