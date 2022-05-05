# Vorverarbeitungsschritt 1: Normalisierung der Pixelwerte
imgs_scaled = pixel_normalization(imgs)

# Vorverarbeitungsschritt 2: Normalisierung der Bounding Boxes
bboxes = bbox_normalization(bboxes, imgs)