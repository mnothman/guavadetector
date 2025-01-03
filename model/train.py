import tensorflow as tf
from tensorflow import keras
from preprocess import load_datasets, augment_data

# Load datasets
BASE_DIR = "../data/archive/GuavaDiseaseDataset"
train_ds, val_ds, test_ds = load_datasets(BASE_DIR)

# Data augmentation
data_augmentation = augment_data()

train_ds = train_ds.map(
    lambda x, y: (data_augmentation(x), y)
).prefetch(buffer_size=tf.data.AUTOTUNE)
val_ds = val_ds.prefetch(buffer_size=tf.data.AUTOTUNE)
test_ds = test_ds.prefetch(buffer_size=tf.data.AUTOTUNE)

# Debugging data pipeline
# for batch in train_ds.take(1):
#     images, labels = batch
#     print(f"Images Shape: {images.shape}, Labels Shape: {labels.shape}")

base_model = keras.applications.MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
base_model.trainable = True
for layer in base_model.layers[:100]:
    layer.trainable = False
print(f"Base Model Output Shape: {base_model.output_shape}")

inputs = keras.layers.Input(shape=(224, 224, 3))
x = base_model(inputs, training=False)
x = keras.layers.GlobalAveragePooling2D()(x)
x = keras.layers.Dense(128, activation='relu')(x)
x = keras.layers.Dropout(0.5)(x)
outputs = keras.layers.Dense(3, activation='softmax')(x)
model = keras.Model(inputs, outputs)
model.summary()

# Compile model
model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

# Train model
history = model.fit(train_ds, validation_data=val_ds, epochs=5)

# Evaluate model
test_loss, test_acc = model.evaluate(test_ds)
print(f"Test accuracy: {test_acc}")

# Save model
model.save('guava_disease_detector.keras')
print("Model saved as guava_disease_detector.keras")
