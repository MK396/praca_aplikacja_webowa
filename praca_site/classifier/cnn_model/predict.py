import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.applications.resnet_v2 import preprocess_input

# __file__ - ścieżka do aktualnego pliku
resnet_path = os.path.join(os.path.dirname(__file__), "resnet50_best_3.keras")
custom_path = os.path.join(os.path.dirname(__file__), "my_best_model_7.keras")
resnet_model = load_model(resnet_path)
custom_model = load_model(custom_path)

class_labels = ['Biodegradowalne', 'Elektroodpady', 'Szkło', 'Zmieszane', 'Papier', 'Metal i tworzywa sztuczne', 'Tekstylia']


def predict_image(img, model_choice):
    if model_choice == 'resnet':
        img = img.resize((128, 128))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)
        model = resnet_model
    else:
        img = img.resize((256, 256))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array/255.0
        model = custom_model

    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)
    confidence = float(predictions[0][predicted_class[0]]) * 100

    return class_labels[predicted_class[0]], round(confidence, 2)
