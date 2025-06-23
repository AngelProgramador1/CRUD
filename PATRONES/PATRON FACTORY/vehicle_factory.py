from typing import Dict, Type
from vehicle import Vehicle
from concrete_vehicles import Car, Motorcycle, Truck

class VehicleFactory:
    """
    Factory para crear diferentes tipos de vehículos.
    Este es el corazón del Patrón Factory.
    """
    
    # Registro de tipos de vehículos disponibles
    _vehicle_types: Dict[str, Type[Vehicle]] = {
        'car': Car,
        'motorcycle': Motorcycle,
        'truck': Truck
    }
    
    @classmethod
    def create_vehicle(cls, vehicle_type: str, brand: str, model: str, **kwargs) -> Vehicle:
        """
        Método Factory principal que crea vehículos según el tipo especificado.
        
        Args:
            vehicle_type: Tipo de vehículo ('car', 'motorcycle', 'truck')
            brand: Marca del vehículo
            model: Modelo del vehículo
            **kwargs: Argumentos adicionales específicos de cada tipo
        
        Returns:
            Vehicle: Instancia del vehículo creado
        
        Raises:
            ValueError: Si el tipo de vehículo no está registrado
        """
        vehicle_type = vehicle_type.lower()
        
        if vehicle_type not in cls._vehicle_types:
            available_types = ', '.join(cls._vehicle_types.keys())
            raise ValueError(f"Tipo de vehículo '{vehicle_type}' no disponible. "
                           f"Tipos disponibles: {available_types}")
        
        # Aquí es donde ocurre la "magia" del Factory:
        # Obtenemos la clase correspondiente y la instanciamos
        vehicle_class = cls._vehicle_types[vehicle_type]
        return vehicle_class(brand, model, **kwargs)
    
    @classmethod
    def register_vehicle_type(cls, name: str, vehicle_class: Type[Vehicle]) -> None:
        """
        Permite registrar nuevos tipos de vehículos dinámicamente.
        Esto hace el Factory extensible sin modificar el código existente.
        """
        cls._vehicle_types[name.lower()] = vehicle_class
    
    @classmethod
    def get_available_types(cls) -> list:
        """Retorna la lista de tipos de vehículos disponibles"""
        return list(cls._vehicle_types.keys())
    
    @classmethod
    def create_car(cls, brand: str, model: str, doors: int = 4) -> Car:
        """Método de conveniencia para crear automóviles"""
        return cls.create_vehicle('car', brand, model, doors=doors)
    
    @classmethod
    def create_motorcycle(cls, brand: str, model: str, engine_size: int = 150) -> Motorcycle:
        """Método de conveniencia para crear motocicletas"""
        return cls.create_vehicle('motorcycle', brand, model, engine_size=engine_size)
    
    @classmethod
    def create_truck(cls, brand: str, model: str, cargo_capacity: float = 10.0) -> Truck:
        """Método de conveniencia para crear camiones"""
        return cls.create_vehicle('truck', brand, model, cargo_capacity=cargo_capacity)