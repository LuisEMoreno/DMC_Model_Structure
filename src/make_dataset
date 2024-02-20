# Script de Preparación de Datos
###################################

import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import LabelEncoder


# Leemos los archivos csv
def read_file_csv(filename):
    df = pd.read_csv(os.path.join('../Data/Raw/', filename))
    print(filename, ' cargado correctamente')
    return df

# Preparamos la data
def data_preparation(df):

  # Eliminamos la columna de CustomerID
  data = df.drop(["customerID"], axis = 1)

  # Eliminamos filas donde el atributo 'Tenure' es 0
  data.drop(labels=data[data["tenure"] == 0].index, axis = 0, inplace = True)

  # Llenamos los datos que faltan en la columna 'TotalCharges' con el promedio.
  data.fillna(data["TotalCharges"].mean())

  # Convertimos la columna 'TotalCharges' a una variable numerica.
  data['TotalCharges'] = pd.to_numeric(data.TotalCharges, errors='coerce')

# Encode Data
def encode_data(dataframe):
    if dataframe.dtype == "object":
        dataframe = LabelEncoder().fit_transform(dataframe)  
    return dataframe

# Exportamos la matriz de datos con las columnas seleccionadas
def data_exporting(df, features, filename):
    dfp = df[features]
    dfp.to_csv(os.path.join('../data/processed/', filename))
    print(filename, 'exportado correctamente en la carpeta processed')

def main():
    # Matriz de Entrenamiento
    df1 = read_file_csv('data.csv')
    tdf1 = data_preparation(df1)
    tdf1_1= tdf1.apply(lambda x: encode_data(x))
    data_exporting(tdf1_1, ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges'], 'data_train.csv')       
          
    # Matriz de Validacion
    df2 = read_file_csv('default_data_new.csv')
    tdf2 = data_preparation(df2)
    tdf2_1= tdf2.apply(lambda x: encode_data(x))
    data_exporting(tdf2_1, ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges'], 'data_val.csv')

    # Matriz de Scoring
    df3 = read_file_csv('default_data_score.csv')
    tdf3 = data_preparation(df3)  
    tdf3_1= tdf3.apply(lambda x: encode_data(x))
    data_exporting(tdf3_1, ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges'], 'data_score.csv')
    
if __name__ == "__main__":
    main()
