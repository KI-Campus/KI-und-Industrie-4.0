# Erstellung eines neuen Trainingsdatensatzes mit den originalen und den augmentierten Bildern  

x_train_aug = np.concatenate((x_train,aug_imgs), axis=0)
bboxes_train_aug = np.concatenate((bboxes_train,aug_bboxes), axis=0)
class_train_aug = np.concatenate((class_train,aug_classes), axis=0)

# Durchmischung der Bilder
x_train_aug, bboxes_train_aug, class_train_aug = shuffle(x_train_aug, bboxes_train_aug, class_train_aug)