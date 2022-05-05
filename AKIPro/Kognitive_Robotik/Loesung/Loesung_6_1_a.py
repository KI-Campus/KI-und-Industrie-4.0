# Wähle zufällig 16 Bilder aus dem Testdatensatz und plotte die korrekten und die vom Netz vorhergesagten Bboxes und Klassen
def plot_example_imgs_pred(x_test, bboxes_test, class_test, img_size, model):
    
    # Wähle zufällig 16 Bilder aus dem Testdatensatz
    myPlotSample = np.array(x_test)
    rnd_sample = np.random.randint(len(myPlotSample), size=16)
    images_show = myPlotSample[rnd_sample]
    
    # korrekte Bounding Boxen und Klassen
    true_bboxes = bboxes_test[rnd_sample]*img_size
    true_class = class_test[rnd_sample]
    
    # Wende das trainierte neuronale Netz an, um Bounding Boxen und Objektklassen für die Testbilder vorherzusagen   
    pred_y = model.predict(images_show)
    pred_bboxes = pred_y[0]*img_size
    pred_class = pred_y[1]
    
    # Plotte testbilder
    plt.figure(figsize=(16, 16))
    for i in range(16):
    
        plt.subplot(4, 4, i+1)
        plt.imshow(images_show[i], origin='lower')
        ax = plt.gca()
    
        # korrekte Bounding Boxen (grün)
        x, y = true_bboxes[i,0], true_bboxes[i,3]
        w, h = (true_bboxes[i,2] - true_bboxes[i,0]), (true_bboxes[i,1] - true_bboxes[i,3])
        box_true = patches.Rectangle((x, y), w, h, linewidth=3, edgecolor='g', facecolor="none")     
        ax.add_patch(box_true)
        
        # vorhergesagte Bounding Boxen (rot) 
        x, y = pred_bboxes[i,0], pred_bboxes[i,3]
        w, h = (pred_bboxes[i,2] - pred_bboxes[i,0]), (pred_bboxes[i,1] - pred_bboxes[i,3])
        box_pred = patches.Rectangle((x, y), w, h, linewidth=3, edgecolor='r', facecolor="none")
        ax.add_patch(box_pred)
    
        # vorhergesagte und korrekte Klasse
        predicted_class_num = np.argmax(pred_class[i])
        true_class_num = np.argmax(true_class[i])
        plt.text(0,x_test.shape[1]+5,class_labels[predicted_class_num], color='r') # vorhergesagte Klasse (grün) 
        plt.text(x_test.shape[2]-100,x_test.shape[1]+5, class_labels[true_class_num], color='g') # korrekte Klasse (rot)
        
    return

plot_example_imgs_pred(x_test, bboxes_test, class_test, img_size, model)