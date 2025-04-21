from scipy.signal import butter, filtfilt

def filtro_pasabanda_butter(inf, sup, fs, orden=5):
    nyquist = 0.5 * fs
    bajo = inf / nyquist
    alto = sup / nyquist
    return butter(orden, [bajo, alto], btype='band')

def aplicar_filtro_pasabanda(datos, inf=0.5, sup=40, fs=256):
    b, a = filtro_pasabanda_butter(inf, sup, fs)
    return filtfilt(b, a, datos, axis=0)
