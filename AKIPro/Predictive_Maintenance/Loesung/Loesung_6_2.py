# Bestimmung der durchschnittlichen Distanz zu den K nächsten Nachbarn für den Trainingsdatensatz
neigh_distance_train, neigh_index_train = knn.kneighbors(X_train)
mean_neigh_distance_train = np.mean(neigh_distance_train, axis=1)

plt.hist(mean_neigh_distance_train,bins=10)
plt.title('Mittlere Distanz zu K nächsten Nachbarn für Trainingsdaten (alle Kugellager i.O.)')
plt.xlabel('mittlere Distanz')
plt.ylabel('#')

# Eine Möglichkeit den Schwellwert festzulegen ist das 99.9% Perzentil zu nehmen
thres_KNN = np.percentile(mean_neigh_distance_train,99.9) 
plt.vlines(thres_KNN,0,80,color='red')
plt.show()
