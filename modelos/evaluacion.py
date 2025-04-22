import pandas as pd
import joblib
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def evaluar_modelo(ruta_csv, ruta_modelo="modelo/modelo_entrenado.pkl"):
    # Cargar modelo entrenado
    modelo = joblib.load(ruta_modelo)

    # Cargar datos de evaluación
    datos = pd.read_csv(ruta_csv)

    # Separar características y etiquetas
    X = datos.drop(columns=["etiqueta"])
    y = datos["etiqueta"]

    # Predicciones
    predicciones = modelo.predict(X)

    # Evaluación
    print("Matriz de Confusión:")
    print(confusion_matrix(y, predicciones))

    print("\nReporte de Clasificación:")
    print(classification_report(y, predicciones))

    print("Precisión global:", accuracy_score(y, predicciones))
