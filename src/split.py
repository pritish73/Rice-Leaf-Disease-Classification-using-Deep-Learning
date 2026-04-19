import os
import shutil
import random
#path
src_dir = r"C:\Users\priti\OneDrive\Desktop\RiceLeaf Disease Recogoniton\data"
base_dir = r"C:\Users\priti\OneDrive\Desktop\RiceLeaf Disease Recogoniton\dataset"
#ratio
train_ratio = 0.7
val_ratio = 0.15
for split in ['train', 'val', 'test']:
    for class_name in os.listdir(src_dir):
        os.makedirs(os.path.join(base_dir, split, class_name), exist_ok=True)
for class_name in os.listdir(src_dir):
    class_path = os.path.join(src_dir, class_name)
    if not os.path.isdir(class_path):
        continue
    images = os.listdir(class_path)
    random.shuffle(images)
    total = len(images)
    train_end = int(train_ratio * total)
    val_end = int((train_ratio + val_ratio) * total)
    train_imgs = images[:train_end]
    val_imgs = images[train_end:val_end]
    test_imgs = images[val_end:]
    for img in train_imgs:
        shutil.copy(os.path.join(class_path, img),
                    os.path.join(base_dir, 'train', class_name, img))
    for img in val_imgs:
        shutil.copy(os.path.join(class_path, img),
                    os.path.join(base_dir, 'val', class_name, img))
    for img in test_imgs:
        shutil.copy(os.path.join(class_path, img),
                    os.path.join(base_dir, 'test', class_name, img))

print("Done")