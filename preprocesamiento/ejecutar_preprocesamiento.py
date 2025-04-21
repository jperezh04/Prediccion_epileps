import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from preprocesamiento.utilidades import cargar_csv, guardar_caracteristicas
from preprocesamiento.filtrado import aplicar_filtro_pasabanda
from preprocesamiento.normalizacion import normalizar_zscore
from preprocesamiento.segmentacion import segmentar_senal
from preprocesamiento.extraccion_caracteristicas import extraer_caracteristicas

FS = 256  # Frecuencia de muestreo
VENTANA = 10  # segundos
PASO = 5      # segundos

carpeta_entrada = os.path.join(os.path.dirname(__file__), '..','ed_to_csv', 'chbmit_data', 'csv_output')
carpeta_entrada = os.path.abspath(carpeta_entrada)

archivo_salida = "caracteristicas_procesadas.csv"

todas_las_caracteristicas = []

for archivo in os.listdir(carpeta_entrada):
    if archivo.endswith(".csv"):
        print(f"Procesando {archivo}...")
        datos = cargar_csv(os.path.join(carpeta_entrada, archivo))
        filtrado = aplicar_filtro_pasabanda(datos, fs=FS)
        normalizado = normalizar_zscore(filtrado)
        ventanas = segmentar_senal(normalizado, VENTANA, PASO, fs=FS)
        for ventana in ventanas:
            caracteristica = extraer_caracteristicas(ventana, fs=FS)
            todas_las_caracteristicas.append(caracteristica)

guardar_caracteristicas(todas_las_caracteristicas, archivo_salida)
print("Preprocesamiento completo.")
