import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array, save_img
#paths
input_dir = r"C:\Users\priti\OneDrive\Desktop\RiceLeaf Disease Recogoniton\data"
output_dir = r"C:\Users\priti\OneDrive\Desktop\RiceLeaf Disease Recogoniton\augmented_data"
os.makedirs(output_dir, exist_ok=True)
#Aug settings
datagen = ImageDataGenerator(
    rotation_range=30,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    vertical_flip=True,
    fill_mode='nearest'
)
for class_name in os.listdir(input_dir):
    class_path = os.path.join(input_dir, class_name)
    if not os.path.isdir(class_path):
        continue
    save_class_path = os.path.join(output_dir, class_name)
    os.makedirs(save_class_path, exist_ok=True)
    print(f"Processing class: {class_name}")
    for img_name in os.listdir(class_path):
        img_path = os.path.join(class_path, img_name)
        try:
            img = load_img(img_path, target_size=(224, 224))
            x = img_to_array(img)
            x = x.reshape((1,) + x.shape)
            #10 aug images per orig
            i = 0
            for batch in datagen.flow(
                x,
                batch_size=1,
                save_to_dir=save_class_path,
                save_prefix='aug',
                save_format='jpg'
            ):
                i += 1
                if i >= 10:
                    break
        except Exception as e:
            print(f"Error processing {img_name}: {e}")
print("Done")