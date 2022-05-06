from IPython.display import Image, display

print("""
Die Daten gehören zum Test-Datensatz. Diese Auswahl macht Sinn, da das neuronale Netz diese Daten während des Trainings nicht sieht.
Zudem sind die Beispiele so gewählt, dass möglichst viele verschiedene Szenarien betrachtet werden. Auch das ist sinnvoll.
""")

img_unsafe = os.path.join("AKIPRO_safety_application_dataset", "unsafe", "akipro_0000002634.jpg")
img_safe_background = os.path.join("AKIPRO_safety_application_dataset", "safe", "akipro_0000000524.jpg")
img_safe_coin_hand = os.path.join("AKIPRO_safety_application_dataset", "safe", "akipro_0000001156.jpg")
img_safe_coin = os.path.join("AKIPRO_safety_application_dataset", "safe", "akipro_0000001666.jpg")

image_paths = [img_unsafe, img_safe_background, img_safe_coin_hand, img_safe_coin]
true_labels = [1, 0, 0, 0]  # safe -> 0, unsafe -> 1

for (img_path, true_label) in zip(image_paths, true_labels):
    img_processed = prepare_image(img_path)
    model_prediction = model.predict(img_processed)
    predicted_label = np.argmax(model_prediction, axis=1)[0]
    certainty = model_prediction[0][predicted_label]

    display(Image(filename=img_path, width=200))
    print(f"Vorhersage: {predicted_label}, Genauigkeit: {certainty:.6f}, Korrekte Klasse: {true_label}")