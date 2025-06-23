from vehicle_factory import VehicleFactory
from vehicle import Vehicle

def demonstrate_factory_pattern():
    """Función que demuestra el uso del Patrón Factory"""
    
    print("=" * 60)
    print("🏭 DEMOSTRACIÓN DEL PATRÓN FACTORY")
    print("=" * 60)
    
    # Lista de vehículos para crear
    vehicles_to_create = [
        ('car', 'Toyota', 'Corolla', {'doors': 4}),
        ('motorcycle', 'Honda', 'CBR600RR', {'engine_size': 600}),
        ('truck', 'Volvo', 'FH16', {'cargo_capacity': 25.0}),
        ('car', 'BMW', 'X5', {'doors': 5}),
        ('motorcycle', 'Yamaha', 'YZF-R1', {'engine_size': 1000})
    ]
    
    vehicles = []
    
    print("\n🔧 CREANDO VEHÍCULOS CON EL FACTORY:")
    print("-" * 40)
    
    for vehicle_type, brand, model, kwargs in vehicles_to_create:
        try:
            # Aquí es donde usamos el Factory Pattern
            vehicle = VehicleFactory.create_vehicle(vehicle_type, brand, model, **kwargs)
            vehicles.append(vehicle)
            print(f"✅ Creado: {vehicle.get_info()}")
        except ValueError as e:
            print(f"❌ Error: {e}")
    
    print(f"\n📊 TOTAL DE VEHÍCULOS CREADOS: {len(vehicles)}")
    
    # Demostrar el polimorfismo
    print("\n🚀 DEMOSTRANDO POLIMORFISMO:")
    print("-" * 40)
    
    for i, vehicle in enumerate(vehicles, 1):
        print(f"\n{i}. {vehicle.get_info()}")
        print(f"   {vehicle.start_engine()}")
        
        # Llamar métodos específicos según el tipo
        if hasattr(vehicle, 'open_trunk'):
            print(f"   {vehicle.open_trunk()}")
        elif hasattr(vehicle, 'wheelie'):
            print(f"   {vehicle.wheelie()}")
        elif hasattr(vehicle, 'load_cargo'):
            print(f"   {vehicle.load_cargo(15.0)}")
    
    # Demostrar métodos de conveniencia
    print("\n🎯 USANDO MÉTODOS DE CONVENIENCIA:")
    print("-" * 40)
    
    sports_car = VehicleFactory.create_car('Ferrari', 'F8 Tributo', doors=2)
    sport_bike = VehicleFactory.create_motorcycle('Ducati', 'Panigale V4', engine_size=1103)
    heavy_truck = VehicleFactory.create_truck('Scania', 'R730', cargo_capacity=40.0)
    
    convenience_vehicles = [sports_car, sport_bike, heavy_truck]
    
    for vehicle in convenience_vehicles:
        print(f"✨ {vehicle.get_info()}")
        print(f"   {vehicle.start_engine()}")
    
    # Mostrar tipos disponibles
    print(f"\n📋 TIPOS DE VEHÍCULOS DISPONIBLES:")
    print(f"   {', '.join(VehicleFactory.get_available_types())}")
    
    # Demostrar manejo de errores
    print("\n⚠️  DEMOSTRANDO MANEJO DE ERRORES:")
    print("-" * 40)
    
    try:
        invalid_vehicle = VehicleFactory.create_vehicle('airplane', 'Boeing', '747')
    except ValueError as e:
        print(f"❌ {e}")

def interactive_vehicle_creator():
    """Función interactiva para crear vehículos"""
    
    print("\n" + "=" * 60)
    print("🎮 CREADOR INTERACTIVO DE VEHÍCULOS")
    print("=" * 60)
    
    available_types = VehicleFactory.get_available_types()
    print(f"Tipos disponibles: {', '.join(available_types)}")
    
    while True:
        print("\n" + "-" * 40)
        vehicle_type = input("Tipo de vehículo (o 'quit' para salir): ").strip().lower()
        
        if vehicle_type == 'quit':
            print("👋 ¡Hasta luego!")
            break
        
        if vehicle_type not in available_types:
            print(f"❌ Tipo inválido. Usa: {', '.join(available_types)}")
            continue
        
        brand = input("Marca: ").strip()
        model = input("Modelo: ").strip()
        
        if not brand or not model:
            print("❌ Marca y modelo son obligatorios")
            continue
        
        try:
            # Parámetros específicos según el tipo
            kwargs = {}
            if vehicle_type == 'car':
                doors = input("Número de puertas (default 4): ").strip()
                if doors:
                    kwargs['doors'] = int(doors)
            elif vehicle_type == 'motorcycle':
                engine = input("Tamaño del motor en cc (default 150): ").strip()
                if engine:
                    kwargs['engine_size'] = int(engine)
            elif vehicle_type == 'truck':
                capacity = input("Capacidad de carga en toneladas (default 10.0): ").strip()
                if capacity:
                    kwargs['cargo_capacity'] = float(capacity)
            
            # Crear el vehículo usando el Factory
            vehicle = VehicleFactory.create_vehicle(vehicle_type, brand, model, **kwargs)
            
            print(f"\n🎉 ¡Vehículo creado exitosamente!")
            print(f"   {vehicle.get_info()}")
            print(f"   {vehicle.start_engine()}")
            
        except (ValueError, TypeError) as e:
            print(f"❌ Error al crear el vehículo: {e}")

if __name__ == "__main__":
    # Ejecutar demostración
    demonstrate_factory_pattern()
    
    # Ejecutar creador interactivo
    interactive_vehicle_creator()