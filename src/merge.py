import os
import shutil
new_base = r"C:\Users\priti\Downloads\archive\RiceLeafs"
main_data = r"C:\Users\priti\OneDrive\Desktop\RiceLeaf Disease Recogoniton\data"
folders_to_merge = ["train", "validation"]
for folder in folders_to_merge:
    folder_path = os.path.join(new_base, folder)
    for class_name in os.listdir(folder_path):
        src_class_path = os.path.join(folder_path, class_name)
        if not os.path.isdir(src_class_path):
            continue
        dst_class_path = os.path.join(main_data, class_name)
        os.makedirs(dst_class_path, exist_ok=True)
        print(f"Merging {folder} → {class_name}")
        for img_name in os.listdir(src_class_path):
            src = os.path.join(src_class_path, img_name)
            dst = os.path.join(dst_class_path, "merged_" + img_name)
            try:
                shutil.copy(src, dst)
            except Exception as e:
                print(e)
print("done")