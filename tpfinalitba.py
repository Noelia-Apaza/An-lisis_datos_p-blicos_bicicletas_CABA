import pandas as pd

# Ruta del archivo original
file_path = r'C:\Users\nicos\Desktop\itba\4.Visualización\TP_Grupal\trips_2023.csv'


# Cargar el CSV con las columnas necesarias
columns = [
    "id_estacion_origen", "nombre_estacion_origen", "direccion_estacion_origen",
    "long_estacion_origen", "lat_estacion_origen", "id_estacion_destino",
    "nombre_estacion_destino", "direccion_estacion_destino", "long_estacion_destino", 
    "lat_estacion_destino"
]

# Leer solo las columnas necesarias para consolidar las estaciones
df = pd.read_csv(file_path, usecols=columns)

# Crear un DataFrame para estaciones origen
df_origen = df[['id_estacion_origen', 'nombre_estacion_origen', 'direccion_estacion_origen', 
                'long_estacion_origen', 'lat_estacion_origen']].drop_duplicates()

df_origen.columns = ['id_estacion', 'nombre_estacion', 'direccion_estacion', 'long_estacion', 'lat_estacion']

# Crear un DataFrame para estaciones destino
df_destino = df[['id_estacion_destino', 'nombre_estacion_destino', 'direccion_estacion_destino', 
                 'long_estacion_destino', 'lat_estacion_destino']].drop_duplicates()

df_destino.columns = ['id_estacion', 'nombre_estacion', 'direccion_estacion', 'long_estacion', 'lat_estacion']

# Concatenar ambos DataFrames de estaciones y eliminar duplicados
df_estaciones = pd.concat([df_origen, df_destino]).drop_duplicates()

# Guardar el archivo consolidado de estaciones
output_estaciones_path = r'C:\Users\nicos\Desktop\itba\4.Visualización\TP_Grupal\estaciones_consolidadasV2.csv'
df_estaciones.to_csv(output_estaciones_path, index=False)

# Para el segundo CSV, cargar el archivo original con las otras columnas
columns_restantes = [
    "Id_recorrido", "duracion_recorrido", "fecha_origen_recorrido", "id_estacion_origen", 
    "fecha_destino_recorrido", "id_estacion_destino", "id_usuario", "modelo_bicicleta", "género"
]

df_restante = pd.read_csv(file_path, usecols=columns_restantes)

# Guardar el archivo con las columnas restantes
output_restante_path = r'C:\Users\nicos\Desktop\itba\4.Visualización\TP_Grupal\recorridos_normalizadosV2.csv'
df_restante.to_csv(output_restante_path, index=False)

print("Archivos generados correctamente:")
print(f"1. {output_estaciones_path}")
print(f"2. {output_restante_path}")
