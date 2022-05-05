n_features = len(X_train[0]) # Anzahl Merkmale 

def get_model():

    autoenc = keras.Sequential()
    init = keras.initializers.glorot_uniform(seed=1)
    # Eingabeschicht und 1. verdeckte Schicht
    autoenc.add(keras.layers.Dense(input_dim=n_features, units=10, activation='tanh', kernel_initializer=init))
    # Ergänzen Sie die 2. verdeckte Schicht
    autoenc.add(keras.layers.Dense(units=5, activation='tanh', kernel_initializer=init))
    # Ergänzen Sie die 3. verdeckte Schicht
    autoenc.add(keras.layers.Dense(units=10, activation='tanh', kernel_initializer=init))
    # output layer
    autoenc.add(keras.layers.Dense(units=n_features, activation='linear', kernel_initializer=init))

    return autoenc

autoenc = get_model()
print('Zusammenfassung des erstellten Modells: \n')
print(autoenc.summary())