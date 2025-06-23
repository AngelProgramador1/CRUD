from abc import ABC, abstractmethod

class Vehicle(ABC):
    """Clase base abstracta para todos los vehículos"""
    
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
    
    @abstractmethod
    def start_engine(self) -> str:
        """Método abstracto para encender el motor"""
        pass
    
    @abstractmethod
    def get_info(self) -> str:
        """Método abstracto para obtener información del vehículo"""
        pass
    
    @abstractmethod
    def get_type(self) -> str:
        """Método abstracto para obtener el tipo de vehículo"""
        pass