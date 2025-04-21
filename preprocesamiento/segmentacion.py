import numpy as np

def segmentar_senal(datos, duracion_ventana, paso, fs):
    muestras_ventana = int(duracion_ventana * fs)
    salto = int(paso * fs)
    ventanas = []

    for inicio in range(0, len(datos) - muestras_ventana + 1, salto):
        fin = inicio + muestras_ventana
        ventana = datos[inicio:fin, :]
        ventanas.append(ventana)

    return np.array(ventanas)
