from sklearn.preprocessing import StandardScaler

def normalizar_zscore(datos):
    escalador = StandardScaler()
    return escalador.fit_transform(datos)
