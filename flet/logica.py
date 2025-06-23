import mysql.connector

config = {
    "user": "root",
    "host": "localhost",
    "port": 3306,
    "password": "AngelGoogle1",
    "database": "a"
}

def get_connection():
    """Obtener una nueva conexión a la base de datos"""
    return mysql.connector.connect(**config)

def consult(table: str, condicion=None):
    conexion = None
    try:
        conexion = get_connection()
        cursor = conexion.cursor()
        
        if condicion:
            query = f"SELECT * FROM {table} WHERE edad < %s"
            cursor.execute(query, condicion)
        else: 
            # Corregido: cuando no hay condición, solo seleccionar todo
            query = f"SELECT * FROM {table}"
            cursor.execute(query)

        result = cursor.fetchall()
        
        # Mostrar nombres de columnas para mejor legibilidad
        column_names = [desc[0] for desc in cursor.description]
        print("Columnas:", column_names)
        print("Resultados:")
        for row in result:
            print(row)
            
        return result
        
    except mysql.connector.Error as err:
        print(f"Error en consulta: {err}")
        return None
    finally:
        if conexion and conexion.is_connected():
            cursor.close()
            conexion.close()

def insertar(nombre: str, edad=None):
    conexion = None
    try:
        conexion = get_connection()
        cursor = conexion.cursor()
        
        if edad is not None:  # Usar 'is not None' en lugar de solo 'edad'
            # Usar parámetros preparados para evitar inyección SQL
            query = "INSERT INTO usuarios (name, edad) VALUES (%s, %s)"
            cursor.execute(query, (nombre, edad))
        else:
            query = "INSERT INTO usuarios (name) VALUES (%s)"
            cursor.execute(query, (nombre,))
        
        # Confirmar los cambios
        conexion.commit()
        print(f"Registro insertado correctamente. ID: {cursor.lastrowid}")
        
    except mysql.connector.Error as err:
        print(f"Error al insertar: {err}")
        if conexion:
            conexion.rollback()
    finally:
        if conexion and conexion.is_connected():
            cursor.close()
            conexion.close()

# Ejemplos de uso
print("=== Consultando usuarios ===")
consult("usuarios", 10)

print("\n=== Insertando nuevo usuario ===")
insertar("angel", 20)

print("\n=== Consultando todos los usuarios ===")
consult("usuarios")