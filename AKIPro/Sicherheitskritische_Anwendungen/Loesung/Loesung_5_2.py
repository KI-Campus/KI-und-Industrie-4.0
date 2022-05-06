print("""
Typische Kurven der Lossfunktion sinken anfangs stark und die Validationslossfunktion, die mit Daten
gespeist wird, auf denen das Netz nicht trainiert, sollte ähnlich zu dieser Kurve verlaufen.
Um mehr über die Kurven der Lossfunktion zu erfahren, speziell wie sie aussehen wenn Overfitting (zu
starke Anpassung an die Trainingsdaten) oder Underfitting (neuronales Netz konnte die Beziehung zwischen
Eingabe und Ausgabe nicht gut lernen) passiert, folgen Sie bitte diesem Link:

https://machinelearningmastery.com/learning-curves-for-diagnosing-machine-learning-model-performance/ (24.11.2021)

Allgemein kann festgehalten werden, dass der Loss Wert die quantifizierte Distanz zur
Ground Truth darstellt. Während die Accuracy repräsentiert, ob das neuronale Netz viele 
oder wenige Fehler bei der Klassifizierung macht. 

Diese Metriken stehen nicht direkt in Beziehung zueinander, aber sie können gemeinsam doch
Aufschluss ergeben, wie gut ein neuronales Netz trainiert. Grob lässt sich sagen:

* geringe Accuracy-Werte und große Loss-Werte -> es wurden auf vielen Datenpunkten viele Fehler bei der Vorhersage der Werte gemacht
* geringe Accuracy-Werte und geringe Loss-Werte -> auf vielen Datenpunkten wurden kleine Fehler begangen
* große Accurracy-Werte und geringe Loss-Werte -> auf wenigen Datenpunkten wurden wenige Fehler begangen (Idealszenario!)
* große Accuracy-Werte und große Loss-Werte -> auf wenigen Datenpunkten wurden große Fehler gemacht


Accuracy-Werte über 50 Prozent bei einer binären Klasse sind oberhalb der Zufallsschwelle. 
Da der Datensatz jedoch unbalanciert ist, verändert sich diese Zufallsschwelle. 
""")