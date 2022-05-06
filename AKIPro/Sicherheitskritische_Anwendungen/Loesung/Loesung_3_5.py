print(df_train.label[:5])
print(train_generator.classes[:5])

print(train_generator.filenames[:5])
print(train_generator.labels[:5])

print("""Die Klasse safe wird durch 0 repräsentiert und die Klasse unsafe durch 1.
Das können Sie herausfinden, indem Sie die Dateipfade des Dataframes den Labels des Generators zuordnen.""")