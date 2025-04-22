import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

def discretizar_etiquetas(datos):
    """
    Convierte las etiquetas a una clasificación binaria:
    - 1 para fase pre-ictal
    - 0 para no pre-ictal
    """
    etiquetas = datos['etiqueta']
    
    # Definir el umbral para separar las clases
    umbral = 2.0  # Este umbral puede variar dependiendo de tu dataset
    
    # Asignar 1 si el valor es mayor que el umbral (fase pre-ictal), 0 si es menor (no pre-ictal)
    datos['etiqueta'] = (etiquetas > umbral).astype(int)
    
    return datos

def entrenar_random_forest(ruta_csv):
    # Cargar el CSV
    nombres_columnas = ['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'etiqueta']
    datos = pd.read_csv(ruta_csv, header=None, names=nombres_columnas)
    
    # Discretizar las etiquetas (pre-ictal y no pre-ictal)
    datos = discretizar_etiquetas(datos)

    # Separar las características y las etiquetas
    X = datos.drop(columns=["etiqueta"])  # características
    y = datos["etiqueta"]  # etiquetas (0 o 1)

    # Dividir en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Crear y entrenar el modelo RandomForestClassifier
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)

    # Hacer predicciones en el conjunto de prueba
    y_pred = modelo.predict(X_test)

    # Evaluar el modelo
    print("Predicciones:", y_pred)
    print("Valores reales:", y_test)
    print("Exactitud:", accuracy_score(y_test, y_pred))
    print("Reporte de clasificación:\n", classification_report(y_test, y_pred))
