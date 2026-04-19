import os
import shutil
data_dir = r"C:\Users\priti\OneDrive\Desktop\RiceLeaf Disease Recogoniton\data"
valid_classes = [
    "Bacterial leaf blight",
    "Brown spot",
    "Leaf smut",
    "Healthy"
]
dup_class = "BrownSpot"
correct_class = "Brown spot"
dup_path = os.path.join(data_dir, dup_class)
correct_path = os.path.join(data_dir, correct_class)
if os.path.exists(dup_path):
    os.makedirs(correct_path, exist_ok=True)
    for img in os.listdir(dup_path):
        shutil.move(
            os.path.join(dup_path, img),
            os.path.join(correct_path, "merged_" + img)
        )
    os.rmdir(dup_path)
for cls in os.listdir(data_dir):
    if cls not in valid_classes:
        shutil.rmtree(os.path.join(data_dir, cls))
        print(f"rem: {cls}")
print("done")