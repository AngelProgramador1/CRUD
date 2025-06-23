"""
Aplicación principal que demuestra el uso del patrón Facade
"""
from facade.home_theater_facade import HomeTheaterFacade

def main():
    print("=== Sistema de Home Theater ===")
    print("Inicializando componentes...")
    
    # Crear la fachada del sistema
    home_theater = HomeTheaterFacade()
    
    print("\n--- INICIANDO PELÍCULA ---")
    home_theater.watch_movie("El Padrino")
    
    print("\n--- PAUSANDO PELÍCULA ---")
    home_theater.pause_movie()
    
    print("\n--- REANUDANDO PELÍCULA ---")
    home_theater.resume_movie()
    
    print("\n--- TERMINANDO PELÍCULA ---")
    home_theater.end_movie()
    
    print("\n--- INICIANDO MÚSICA ---")
    home_theater.listen_music("Playlist de Jazz")
    
    print("\n--- TERMINANDO MÚSICA ---")
    home_theater.end_music()

if __name__ == "__main__":
    main()