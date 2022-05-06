# Bild der sicheren Kategorie laden
img_path = os.path.join(safe_dir, "akipro_0000000000.jpg")
img = cv2.imread(img_path)

# Bild der sicheren Kategorie anzeigen
plt.imshow(img[:, :, ::-1])
plt.xticks([]), plt.yticks([])  # Dadurch werden keine Striche an den Achsen angezeigt
plt.title("sicher")
plt.show()

# Bild der unsicheren Kategorie laden
img_path = os.path.join(unsafe_dir, "akipro_0000002085.jpg")
img = cv2.imread(img_path)

# Bild der unsicheren Kategorie anzeigen
plt.imshow(img[:, :, ::-1])
plt.xticks([]), plt.yticks([])  # Dadurch werden keine Striche an den Achsen angezeigt
plt.title("unsicher")
plt.show()

# Maximal- und Minimalwerte des Bildes
print(f"Maximum der Bildwerte: {np.max(img)}, , Minimum der Bildwerte: {np.min(img)}")

# Größe des Bildes
print(f"Größe des Bildes: {img.shape}")