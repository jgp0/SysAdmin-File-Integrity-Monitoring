import hashlib
import os
import csv
import time

# Directorio a monitorear (puedes personalizar esta ruta)
directorio_monitoreado = 'test/'

# Archivo CSV para almacenar los registros de hashes
archivo_registros = 'data/registros_hashes.csv'

# Conjunto para almacenar nombres de archivos procesados
archivos_procesados = set()

# Función para calcular el hash de un archivo
def calcular_hash(archivo):
    sha256 = hashlib.sha256()
    with open(archivo, 'rb') as f:
        while True:
            bloque = f.read(65536)  # Leer en bloques de 64 KB
            if not bloque:
                break
            sha256.update(bloque)
    return sha256.hexdigest()

# Función para cargar los registros de hashes desde el archivo CSV
def cargar_registros():
    registros = set()
    if os.path.exists(archivo_registros):
        with open(archivo_registros, 'r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            for fila in lector_csv:
                registros.add((fila[0], fila[1], fila[2]))  # (hash, fecha_hora, ruta)
    return registros

# Función para guardar un registro en el archivo CSV
def guardar_registro(registro):
    with open(archivo_registros, 'a', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(registro)

# Función para monitorear la integridad de los archivos
def monitorear_integridad():
    print("Iniciando monitoreo de integridad de archivos...")
    registros = cargar_registros()

    while True:
        time.sleep(1)  # Pausa entre verificaciones

        for ruta_actual, _, archivos in os.walk(directorio_monitoreado):
            for archivo in archivos:
                ruta_completa = os.path.join(ruta_actual, archivo)
                hash_actual = calcular_hash(ruta_completa)

                # Verificar si el archivo ya ha sido procesado
                if ruta_completa in archivos_procesados:
                    continue

                # Verificar si el archivo ha cambiado
                if (hash_actual, ruta_completa) not in registros:
                    fecha_hora = time.strftime("%Y-%m-%d %H:%M:%S")
                    registro = (hash_actual, fecha_hora, ruta_completa)
                    guardar_registro(registro)
                    archivos_procesados.add(ruta_completa)  # Agregar a archivos procesados
                    print(f"¡Alerta! El archivo {ruta_completa} ha sido modificado.")

# Función principal
if __name__ == '__main__':
    monitorear_integridad()