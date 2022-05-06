def plot_heatmap(fig, img, heatmap, model, title, plot_idx, rows=2, cols=2):
    logit = model.predict(img)
    label = np.argmax(logit, axis=1).item()
    x_label = f"label: {label},  mit Sicherheit: {logit[0][label]:.6f}"

    fig.add_subplot(rows, columns, plot_idx)
    plt.title(title)
    plt.imshow(img[0,:,:, :])
    plt.imshow(heatmap, alpha=0.5)
    plt.xlabel(x_label)
    plt.xticks([])
    plt.yticks([])

# Bilder laden
img_safe_background_processed = prepare_image(img_safe_background)
img_safe_coin_hand_processed = prepare_image(img_safe_coin_hand)
img_safe_coin_processed = prepare_image(img_safe_coin)
img_unsafe_processed = prepare_image(img_unsafe)

# Plot Einstellungen
rows, columns = 2, 2
fig = plt.figure(figsize=(15, 10))
fig.suptitle('Attention Maps')

# Bilder mit Heatmaps plotten
plot_heatmap(fig, img_safe_background_processed, attention_map_safe_background, model, "Bild mit Hintergrund", 1)
plot_heatmap(fig, img_safe_coin_hand_processed, attention_map_safe_coin_hand, model, "Bild mit Hintergrund", 2)
plot_heatmap(fig, img_safe_coin_processed, attention_map_safe_coin, model, "Bild mit Hintergrund", 3)
plot_heatmap(fig, img_unsafe_processed, attention_map_unsafe, model, "Bild mit Hintergrund", 4)
plt.show()
