import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras import layers, models
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
#path
train_dir = r"C:\Users\priti\OneDrive\Desktop\RiceLeaf Disease Recogoniton\dataset\train"
val_dir   = r"C:\Users\priti\OneDrive\Desktop\RiceLeaf Disease Recogoniton\dataset\val"
test_dir  = r"C:\Users\priti\OneDrive\Desktop\RiceLeaf Disease Recogoniton\dataset\test"
IMG_SIZE = (256, 256)
BATCH_SIZE = 16
train_datagen = ImageDataGenerator(                 #aug
    rescale=1./255,
    rotation_range=20,
    zoom_range=0.15,
    shear_range=0.1,
    horizontal_flip=True,
    brightness_range=[0.85, 1.15]
)
val_test_datagen = ImageDataGenerator(rescale=1./255)
train_gen = train_datagen.flow_from_directory(
    train_dir,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)
val_gen = val_test_datagen.flow_from_directory(
    val_dir,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)
test_gen = val_test_datagen.flow_from_directory(
    test_dir,
    target_size=IMG_SIZE,
    batch_size=1,
    class_mode='categorical',
    shuffle=False
)
base_model = MobileNetV2(
    weights='imagenet',
    include_top=False,
    input_shape=(224, 224, 3)
)
for layer in base_model.layers:
    layer.trainable = False
x = base_model.output
x = layers.GlobalAveragePooling2D()(x)
x = layers.BatchNormalization()(x)
x = layers.Dense(128, activation='relu')(x)
x = layers.Dropout(0.5)(x)
outputs = layers.Dense(train_gen.num_classes, activation='softmax')(x)
model = models.Model(inputs=base_model.input, outputs=outputs)
model.compile(
    optimizer=Adam(learning_rate=1e-6),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)
early_stop = EarlyStopping(patience=3, restore_best_weights=True)
reduce_lr = ReduceLROnPlateau(patience=2, factor=0.3)
history = model.fit(                #train
    train_gen,
    validation_data=val_gen,
    epochs=15,                                  #set epoch
    callbacks=[early_stop, reduce_lr]
)
for layer in base_model.layers[-15:]:      #tune
    layer.trainable = True
model.compile(
    optimizer=Adam(learning_rate=1e-5),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)
history_fine = model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=10,
    callbacks=[early_stop, reduce_lr]
)
test_loss, test_acc = model.evaluate(test_gen)
print("\nfinal acc", round(test_acc, 4))
model.save("rice_model.h5")