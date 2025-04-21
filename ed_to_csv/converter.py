import os
import pandas as pd
import pyedflib

def convert_edf_to_csv(edf_path, output_folder):
    try:
        f = pyedflib.EdfReader(edf_path)
        n_signals = f.signals_in_file
        signal_labels = f.getSignalLabels()
        data = {}

        for i in range(n_signals):
            signal = f.readSignal(i)
            label = signal_labels[i]
            data[label] = signal

        df = pd.DataFrame(data)
        file_name = os.path.splitext(os.path.basename(edf_path))[0] + ".csv"
        output_path = os.path.join(output_folder, file_name)
        df.to_csv(output_path, index=False)
        print(f"✅ Guardado: {file_name}")
        f.close()

    except Exception as e:
        print(f"Error al convertir {edf_path}: {e}")

def convert_all_edfs_in_folder(folder_path):
    output_folder = os.path.join(folder_path, "csv_output")
    os.makedirs(output_folder, exist_ok=True)

    print(f"🔍 Buscando archivos EDF en: {folder_path}")
    edf_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".edf"):
                edf_files.append(os.path.join(root, file))

    print(f"📁 {len(edf_files)} archivo(s) EDF encontrados.\n")

    for edf_file in edf_files:
        print(f"Convirtiendo: {os.path.basename(edf_file)}")
        convert_edf_to_csv(edf_file, output_folder)

    print("\nConversión finalizada.")

if __name__ == "__main__":
    ruta = "C:/Users/Jeremy/IA-Proyectos/Proy1/ed_to_csv/chbmit_data"

    if os.path.exists(ruta):
        convert_all_edfs_in_folder(ruta)
    else:
        print("Ruta no válida. Asegúrate de que exista.")
