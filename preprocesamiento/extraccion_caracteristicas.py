import numpy as np
from scipy.signal import welch
from scipy.stats import entropy

def potencia_banda(dato, fs, banda):
    frecuencias, psd = welch(dato, fs)
    indices = np.logical_and(frecuencias >= banda[0], frecuencias <= banda[1])
    return np.mean(psd[:, indices], axis=1)

def extraer_caracteristicas(ventana, fs=256):
    caracteristicas = []
    for canal in ventana.T:
        potencias = [
            potencia_banda(canal[np.newaxis, :], fs, b)[0]
            for b in [(0.5,4),(4,8),(8,13),(13,30),(30,45)]
        ]
        energia = np.sum(np.square(canal))
        entropia = entropy(np.histogram(canal, bins=20)[0] + 1)
        caracteristicas.append(potencias + [energia, entropia])
    return np.mean(caracteristicas, axis=0)
