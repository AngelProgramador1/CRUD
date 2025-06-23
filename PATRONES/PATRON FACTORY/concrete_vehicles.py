from vehicle import Vehicle

class Car(Vehicle):
    """Implementación concreta de un automóvil"""
    
    def __init__(self, brand: str, model: str, doors: int = 4):
        super().__init__(brand, model)
        self.doors = doors
    
    def start_engine(self) -> str:
        return f"🚗 El automóvil {self.brand} {self.model} está encendiendo con llave..."
    
    def get_info(self) -> str:
        return f"Automóvil: {self.brand} {self.model} - {self.doors} puertas"
    
    def get_type(self) -> str:
        return "Automóvil"
    
    def open_trunk(self) -> str:
        return f"Abriendo el maletero del {self.brand} {self.model}"

class Motorcycle(Vehicle):
    """Implementación concreta de una motocicleta"""
    
    def __init__(self, brand: str, model: str, engine_size: int = 150):
        super().__init__(brand, model)
        self.engine_size = engine_size
    
    def start_engine(self) -> str:
        return f"🏍️ La motocicleta {self.brand} {self.model} está encendiendo con botón..."
    
    def get_info(self) -> str:
        return f"Motocicleta: {self.brand} {self.model} - {self.engine_size}cc"
    
    def get_type(self) -> str:
        return "Motocicleta"
    
    def wheelie(self) -> str:
        return f"¡{self.brand} {self.model} haciendo caballito! 🤘"

class Truck(Vehicle):
    """Implementación concreta de un camión"""
    
    def __init__(self, brand: str, model: str, cargo_capacity: float = 10.0):
        super().__init__(brand, model)
        self.cargo_capacity = cargo_capacity
    
    def start_engine(self) -> str:
        return f"🚛 El camión {self.brand} {self.model} está encendiendo (motor diésel)..."
    
    def get_info(self) -> str:
        return f"Camión: {self.brand} {self.model} - Capacidad: {self.cargo_capacity} toneladas"
    
    def get_type(self) -> str:
        return "Camión"
    
    def load_cargo(self, weight: float) -> str:
        if weight <= self.cargo_capacity:
            return f"Cargando {weight} toneladas en el {self.brand} {self.model}"
        else:
            return f"¡Sobrecarga! El {self.brand} {self.model} solo puede cargar {self.cargo_capacity} toneladas"