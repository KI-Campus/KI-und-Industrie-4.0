# Aufteilung der Daten in Trainings- und Testdatensatz

train_idx = np.where(date<np.datetime64('2004-02-14'))[0] # Nummern der Dateien, die zum Trainingsdatensatz gehören   
test_idx = np.where(date>=np.datetime64('2004-02-14'))[0]                    

X_train = X[train_idx] # Trainingsdaten
X_test = X[test_idx] 