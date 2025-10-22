import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.applications.resnet_v2 import preprocess_input

# __file__ - ścieżka aktualnego pliku
model_path = os.path.join(os.path.dirname(__file__), "resnet50_best_3.keras")

model = load_model(model_path)

class_labels = ['Bio', 'Elektrośmieci', 'Szkło', 'Zmieszane', 'Papier', 'Metal i tworzywa sztuczne', 'Ubrania']

# Funkcja przyjmująca ścieżkę do obrazu i zwracająca przewidywaną klasę
def predict_image(img_path):
    img = image.load_img(img_path, target_size=(128, 128))
    # konwersja obrazu do tablicy
    img_array = image.img_to_array(img)
    # axis=0 dodaje wymiar batch
    img_array = np.expand_dims(img_array, axis=0)
    # jesli trenowano z rescale = 1./255 to odkomentuj
    #img_array = img_array/255.0
    img_array = preprocess_input(img_array)

    # wykonanie predykcji, zwraca wektor prawdopodobieństw
    predictions = model.predict(img_array)
    # axis=1 bo mamy batch
    predicted_class = np.argmax(predictions, axis=1)

    # predictions[0][predicted_class[0]] → wartość w tej liście odpowiadająca najbardziej prawdopodobnej klasie
    confidence = float(predictions[0][predicted_class[0]]) * 100
    # jesli predicted_class[0] == 1 to klasa 1 czyli electro
    return class_labels[predicted_class[0]], round(confidence, 2)
