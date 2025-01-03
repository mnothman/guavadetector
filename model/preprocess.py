import tensorflow as tf

def load_datasets(base_dir, img_size=(224, 224), batch_size=32):
    """
    Loads training, validation, and test datasets from the directory structure.

    Args:
        base_dir (str): Base directory containing 'train', 'val', and 'test' folders.
        img_size (tuple): Target size for resizing images.
        batch_size (int): Number of samples per batch.

    Returns:
        Tuple: Prepared training, validation, and test datasets.
    """
    train_dir = f"{base_dir}/train"
    val_dir = f"{base_dir}/val"
    test_dir = f"{base_dir}/test"
    print("Train Directory:", train_dir)
    print("Validation Directory:", val_dir)
    print("Test Directory:", test_dir)

    train_ds = tf.keras.utils.image_dataset_from_directory(
        train_dir,
        image_size=img_size,
        batch_size=batch_size,
        label_mode='categorical'
    )

    val_ds = tf.keras.utils.image_dataset_from_directory(
        val_dir,
        image_size=img_size,
        batch_size=batch_size,
        label_mode='categorical'
    )

    test_ds = tf.keras.utils.image_dataset_from_directory(
        test_dir,
        image_size=img_size,
        batch_size=batch_size,
        label_mode='categorical'
    )
    print("Classes:", train_ds.class_names)

    # Normalize pixel values for all of the datasets
    normalization_layer = tf.keras.layers.Rescaling(1./255)
    train_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
    val_ds = val_ds.map(lambda x, y: (normalization_layer(x), y))
    test_ds = test_ds.map(lambda x, y: (normalization_layer(x), y))

    # Prefetch data for improved performance
    train_ds = train_ds.prefetch(buffer_size=tf.data.AUTOTUNE)
    val_ds = val_ds.prefetch(buffer_size=tf.data.AUTOTUNE)
    test_ds = test_ds.prefetch(buffer_size=tf.data.AUTOTUNE)

    return train_ds, val_ds, test_ds

def augment_data():
    """
    Creates a data augmentation pipeline for training.

    Returns:
        tf.keras.Sequential: A sequential model containing augmentation layers.
    """
    return tf.keras.Sequential([
        tf.keras.layers.RandomFlip("horizontal"),
        tf.keras.layers.RandomRotation(0.2),
        tf.keras.layers.RandomZoom(0.1),
    ])
