lr = 0.001 # Lernrate
num_epochs = 20 # Anzahl Epochen - Die Anzahl der Epochen wurde halbiert. Da der Trainingsdatensatz nun doppelt so groß ist, sind weniger Epochen für das Training notwendig. 
batch_size = 64 # Batch size

# Gewichtung der Fehler 
w_1 = 10.0 # Lokalisierung
w_2 = 1.0 # Klassifizierung

# Laden der zufälligen Startgewichte des Netzes  
model.load_weights('model_default_weights.h5')

opt = Adam(learning_rate=lr)

model.compile(loss={'output_bb' : 'mean_squared_error', 'output_class' : 'categorical_crossentropy'}, 
              loss_weights=[w_1,w_2],
              optimizer=opt, 
              metrics=['accuracy'])

model_checkpoint_callback = ModelCheckpoint(
                            filepath="my_model_aug.h5", # diese Zeile wurde bereits geändert, um das alte Modell nicht zu überschreiben
                            monitor='val_loss',
                            mode='min',
                            save_best_only=True,
                            save_weights_only=False)

history = model.fit(
                    x_train_aug,
                    (bboxes_train_aug, class_train_aug), # Hier wurde der alte durch den neuen Datensatz ersetzt
                    batch_size=batch_size,
                    epochs=num_epochs,
                    callbacks=[model_checkpoint_callback],
                    validation_split=0.2)