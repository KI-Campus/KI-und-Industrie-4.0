def create_csv_file(dir):
    # Zunächst werden die Pfade definiert. Bitte ergänzen Sie die Zeile für das Test.csv
    csv_path_train = os.path.join(dir, "Training.csv")
    csv_path_test = os.path.join(dir, "Test.csv")

    # Jetzt werden die Dateien erstellt und die Spaltennamen geschrieben
    # Training
    with open(csv_path_train, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ImageId", "PredictionString"])
    # Test
    with open(csv_path_test, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ImageId", "PredictionString"])

    # Anzeigen der verschiedenen Klassen -> Es werden nur die Ordner verwendet
    list_of_classes = [element for element in os.listdir(dir) if not os.path.isfile(os.path.join(dir, element))]
    print(f"Liste aller Klassen: {str(list_of_classes)}")

    # Iteriere über alle Klassen
    for current_class in list_of_classes:
        class_dir = os.path.join(dir, current_class)
        # Liste aller .jpg Dateien im Ordner der aktuellen Klasse
        #for file in os.listdir(class_dir)
        list_of_files = [file for file in os.listdir(class_dir) if os.path.isfile(os.path.join(class_dir, file)) and file.endswith(".jpg")]
        
        # Dateien zufällig mischen
        random.seed(0)
        random.shuffle(list_of_files)

        # Dateien in Trainings- und Testdaten splitten
        train_end = int(len(list_of_files) * 0.75)
        train_files = list_of_files[:train_end]
        test_files = list_of_files[train_end:]

        # Hier werden die Dateiname in die .csv Dateien geschrieben
        # Training
        with open(csv_path_train, 'a', newline='') as file:
            writer = csv.writer(file)
            for file in train_files:
                writer.writerow([file, current_class])

        # Test
        with open(csv_path_test, 'a', newline='') as file:
            writer = csv.writer(file)
            for file in test_files:
                writer.writerow([file, current_class])


# Verzeichnis, in dem der Datensatz liegt
input_dir = 'AKIPRO_safety_application_dataset'

# Erstellen der .csv Dateien
create_csv_file(input_dir)