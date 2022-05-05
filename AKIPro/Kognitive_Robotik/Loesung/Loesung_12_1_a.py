# Aufteilung der Daten in Trainings- und Testdaten 

# Durchmischen der Daten vor der Aufteilung  
imgs_scaled = np.array(imgs_scaled)
imgs_scaled, bboxes, classes = shuffle(imgs_scaled, bboxes, classes)

n_train = int(0.8 * num_imgs) #Anzahl der Bilder, die zum Trainingsdatensatz gehören sollen

# Trainingsdaten
x_train = imgs_scaled[:n_train] # Die ersten n_train Bilder gehören zum Trainingsdatensatz
bboxes_train = bboxes[:n_train]
class_train = classes[:n_train]

# Testdaten 
x_test = imgs_scaled[n_train:] # Die restlichen Bilder gehören zum Testdatensatz
bboxes_test = bboxes[n_train:]
class_test = classes[n_train:]

print("Anzahl Bilder Trainingsdatensatz: ", len(x_train))
print("Anzahl Bilder Testdatensatz: ", len(x_test))