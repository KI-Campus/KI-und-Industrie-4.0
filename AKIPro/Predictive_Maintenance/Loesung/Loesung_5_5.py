pred = autoenc.predict(X_train)
error = mae(X_train, pred)

plt.hist(error,bins=10)
plt.title('Fehler für Trainingsdaten (alle Kugellager i.O.)')
plt.xlabel('MAE')
plt.ylabel('#')

# Eine Möglichkeit den Schwellwert festzulegen ist das 99% Perzentil der Trainingsdaten zu nehmen. 
thres = np.percentile(error,99)
plt.vlines(thres,0,50,color='red')
plt.show()