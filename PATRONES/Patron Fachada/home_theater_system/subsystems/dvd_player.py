"""
Subsistema: Reproductor DVD
Maneja la reproducción de medios físicos
"""

class DVDPlayer:
    """Reproductor DVD con controles básicos"""
    
    def __init__(self):
        self.is_on = False
        self.current_movie = None
        self.is_playing = False
        self.is_paused = False
    
    def on(self):
        self.is_on = True
        print("📀 Reproductor DVD encendido")
    
    def off(self):
        self.is_on = False
        self.current_movie = None
        self.is_playing = False
        print("📀 Reproductor DVD apagado")
    
    def play(self, movie_title: str = None):
        if not self.is_on:
            print("📀 Error: Reproductor DVD está apagado")
            return
        
        if movie_title:
            self.current_movie = movie_title
            print(f"📀 Insertando DVD: {movie_title}")
        
        if self.current_movie:
            self.is_playing = True
            self.is_paused = False
            print(f"📀 Reproduciendo: {self.current_movie}")
        else:
            print("📀 No hay película para reproducir")
    
    def pause(self):
        if self.is_playing:
            self.is_paused = True
            self.is_playing = False
            print("📀 Reproducción pausada")
    
    def stop(self):
        self.is_playing = False
        self.is_paused = False
        print("📀 Reproducción detenida")
    
    def eject(self):
        self.stop()
        self.current_movie = None
        print("📀 DVD expulsado")