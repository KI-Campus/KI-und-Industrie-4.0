print("""
Das neuronale Netz hat 5 Schichten. (Die Batch_Norm Ebene wird nicht mitgezählt, da sie meistens zur Faltung
als zugehörig gilt, wenn sie denn verwendet wird.) Die Batch_Norm besitzt trainierbare Parameter. 
Für nähere Informationen kann auch dieser Link besucht werden:

https://kratzert.github.io/2016/02/12/understanding-the-gradient-flow-through-the-batch-normalization-layer.html (24.11.2021)

Andere Operationen, wie z.B. Max_Pooling2D() oder Flatten() sind Operationen, die zwischen den Ebenen 
stattfinden und auch nicht extra gezählt werden. 

model.summary() berechnet für uns die Anzahl der Parameter. Aber wer selbst nachrechnen
möchte, der kann folgenden Link folgen, um mehr Informationen zu erhalten. Beachten Sie dabei,
dass Parameter wie "stride" bei der Faltung die Anzahl der Parameter stark beeinflussen kann. 

https://medium.com/@iamvarman/how-to-calculate-the-number-of-parameters-in-the-cnn-5bd55364d7ca (24.11.2021)

""")