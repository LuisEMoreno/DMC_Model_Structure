from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier


# Cargar la tabla transformada
def read_file_csv(filename):
    df = pd.read_csv(os.path.join('../data/processed', filename))
    X = df.drop(columns = "Churn")
    y = df["Churn"].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 4, stratify =y)
    print(filename, ' cargado correctamente')
    # Entrenamos el modelo con toda la muestra
    X_train[col] = StandardScaler().fit_transform(X_train[col])
    X_test[col] = StandardScaler().fit_transform(X_test[col])
    ada = AdaBoostClassifier()
    ada.fit(X_train, y_train)
    print('Modelo entrenado')
    # Guardamos el modelo entrenado para usarlo en produccion
    package = '../models/best_model.pkl'
    pickle.dump(adaboost_model, open(package, 'wb'))
    print('Modelo exportado correctamente en la carpeta models')

# Entrenamiento completo
def main():
    read_file_csv('data_train.csv')
    print('Finalizó el entrenamiento del Modelo')


if __name__ == "__main__":
    main()
