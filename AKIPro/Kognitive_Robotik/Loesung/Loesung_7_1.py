# Definition verschiedener Augmentierungsfunktionen  
    
# Bilder aufhellen
def brightness(image):
    max_val = 1-np.min(image)-0.1
    bright = np.random.random(1)*max_val
    im_bright = image + bright
    im_bright = np.clip(im_bright, 0.0, 1.0)
    return im_bright

# Bilder abdunkeln
def darkness(image):
    max_val = np.min(image)
    dark = np.random.random(1)*max_val
    im_dark = image - dark
    im_dark = np.clip(im_dark, 0.0, 1.0)
    return im_dark

# Rauschen hinzufügen
def noise(image):
    amount = np.random.uniform(0.0,0.05,1)
    im_noise = random_noise(image, mode='s&p', clip=True, amount=amount[0])
    return im_noise 
    
# Unschärfe hinzufügen
def blur(image):
    rand = np.random.randint(0,5)
    im_blur = cv.GaussianBlur(image,(5,5), rand)
    return(im_blur)

# Testbild augmentieren
original_img = x_test[0]
augmented_img = brightness(original_img) # brightness kann hier durch die anderen definierten Funktionen ersetzt werden

# Visualisierung 
plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1, title="original")
plt.imshow(original_img, origin="lower")
plt.subplot(1, 2, 2, title="augmented")
plt.imshow(augmented_img, origin="lower")