import pandas as pd
import os

def cargar_csv(ruta):
    return pd.read_csv(ruta).values

def guardar_caracteristicas(caracteristicas, salida):
    df = pd.DataFrame(caracteristicas)
    df.to_csv(salida, index=False)
