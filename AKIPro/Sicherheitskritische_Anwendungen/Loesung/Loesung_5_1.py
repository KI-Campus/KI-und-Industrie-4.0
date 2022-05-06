import ast

history_path = os.path.join(model_dir, "model_akipro_security.ckpt_lr-0-0001_history.txt")
with open(history_path, 'r') as file:
    history = file.readlines()

# Kovertieren als Dictionary
hist_dict = ast.literal_eval(history[0])

# Laden in separate Listen
train_loss = hist_dict["loss"]
val_loss = hist_dict["val_loss"]
train_acc = hist_dict["acc"]
val_acc = hist_dict["val_acc"]

# Loss-Kurve
plt.plot(train_loss, label="train_loss")
plt.plot(val_loss, label="val_loss")
plt.legend()
plt.xlabel("epoch")
plt.ylabel("loss")
plt.title("Loss-Kurve")
plt.show()

# Accuracy-Kurve
plt.plot(train_acc, label="train_loss")
plt.plot(val_acc, label="val_loss")
plt.legend()
plt.xlabel("epoch")
plt.ylabel("accuracy")
plt.title("Accuracy-Kurve")
plt.show()