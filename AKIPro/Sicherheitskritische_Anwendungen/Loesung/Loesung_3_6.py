safe_count, unsafe_count = 0, 0

for idx, data_row in df_train.iterrows():
    label = data_row["label"]
    if label == "safe":
        safe_count += 1
    else:
        unsafe_count += 1

print(f"Die sichere Klasse beinhaltet {safe_count} Bilder.")
print(f"Die unsichere Klasse beinhaltet {unsafe_count} Bilder.")