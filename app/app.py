from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np
import cv2

app = Flask(__name__)
model = tf.keras.models.load_model('../model/guava_disease_detector.keras')

categories = ['Anthracnose', 'Fruit Fly', 'Healthy']

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    
    if img is None:
        raise ValueError("Image not found or unable to read the image at path: " + image_path)

    img_resized = cv2.resize(img, (224, 224))

    img_normalized = img_resized / 255.0

    # Batch dimensions (model expects shape:(1, 224, 224, 3)
    img_with_batch = np.expand_dims(img_normalized, axis=0)

    print("Preprocessed input shape for prediction:", img_with_batch.shape)

    return img_with_batch 

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            file_path = './static/' + file.filename
            file.save(file_path)
            img = preprocess_image(file_path)
            try:
                prediction = model.predict(img)
                class_index = np.argmax(prediction)
                class_name = categories[class_index]
                prediction_score = prediction[0][class_index]  # Confidence score
                return render_template(
                    'upload.html', 
                    prediction=class_name, 
                    score=round(prediction_score, 2),  # Round the score for readability
                    image=file.filename
                )
            except Exception as e:
                return render_template('upload.html', error=str(e))
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
