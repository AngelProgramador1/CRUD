"""
Facade (Fachada) del Sistema de Home Theater
Esta clase proporciona una interfaz simplificada para interactuar
con todos los subsistemas complejos del home theater.
"""
from subsystems.amplifier import Amplifier
from subsystems.dvd_player import DVDPlayer
from subsystems.projector import Projector
from subsystems.screen import Screen
from subsystems.theater_lights import TheaterLights
from subsystems.popcorn_popper import PopcornPopper

class HomeTheaterFacade:
    """
    Facade que simplifica la interacción con múltiples subsistemas
    del home theater proporcionando métodos de alto nivel.
    """
    
    def __init__(self):
        """Inicializa todos los subsistemas"""
        self.amplifier = Amplifier()
        self.dvd_player = DVDPlayer()
        self.projector = Projector()
        self.screen = Screen()
        self.lights = TheaterLights()
        self.popcorn_popper = PopcornPopper()
    
    def watch_movie(self, movie_title: str):
        """
        Método de alto nivel para iniciar una película.
        Coordina múltiples subsistemas con una sola llamada.
        """
        print(f"Preparando el sistema para ver: {movie_title}")
        
        # Secuencia compleja coordinada por la fachada
        self.popcorn_popper.on()
        self.popcorn_popper.pop()
        
        self.lights.dim(10)
        self.screen.down()
        
        self.projector.on()
        self.projector.wide_screen_mode()
        
        self.amplifier.on()
        self.amplifier.set_dvd()
        self.amplifier.set_surround_sound()
        self.amplifier.set_volume(8)
        
        self.dvd_player.on()
        self.dvd_player.play(movie_title)
        
        print("¡Sistema listo! Disfruta la película 🎬")
    
    def pause_movie(self):
        """Pausa la película y ajusta la iluminación"""
        print("Pausando película...")
        self.dvd_player.pause()
        self.lights.dim(30)
        print("Película pausada ⏸️")
    
    def resume_movie(self):
        """Reanuda la película y restaura la configuración"""
        print("Reanudando película...")
        self.lights.dim(10)
        self.dvd_player.play()
        print("Película reanudada ▶️")
    
    def end_movie(self):
        """
        Apaga todos los sistemas al finalizar la película.
        Otra operación compleja simplificada.
        """
        print("Finalizando película y apagando sistema...")
        
        self.popcorn_popper.off()
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amplifier.off()
        self.dvd_player.stop()
        self.dvd_player.off()
        
        print("Sistema apagado. ¡Gracias por usar nuestro Home Theater! 👋")
    
    def listen_music(self, playlist: str):
        """Configura el sistema para escuchar música"""
        print(f"Configurando sistema para música: {playlist}")
        
        self.amplifier.on()
        self.amplifier.set_stereo_sound()
        self.amplifier.set_volume(6)
        self.lights.dim(40)
        
        # Simulamos reproducir desde un servicio de streaming
        print(f"🎵 Reproduciendo: {playlist}")
        print("Sistema de música configurado")
    
    def end_music(self):
        """Termina la reproducción de música"""
        print("Terminando reproducción de música...")
        self.amplifier.off()
        self.lights.on()
        print("Música terminada 🎵")