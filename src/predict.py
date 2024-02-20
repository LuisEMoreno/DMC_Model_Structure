import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
import pickle
import os


# Cargar la tabla transformada
def score_model(filename, scores):
    df = pd.read_csv(os.path.join('../Data/Processed', filename))
    print(filename, ' cargado correctamente')
    # Leemos el modelo entrenado para usarlo
    package = '../models/best_model.pkl'
    model = pickle.load(open(package, 'rb'))
    print('Modelo importado correctamente')
    # Predecimos sobre el set de datos de Scoring    
    y_pred = model.predict(X_test)
    pred = pd.DataFrame(y_pred, columns=['PREDICT'])
    pred.to_csv(os.path.join('../Data/Scores/', scores))
    print(scores, 'exportado correctamente en la carpeta scores')


# Scoring desde el inicio
def main():
    df = score_model('data_score.csv','final_score.csv')
    print('Finalizó el Scoring del Modelo')


if __name__ == "__main__":
    main()
