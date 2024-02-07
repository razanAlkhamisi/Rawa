import os
from io import BytesIO

import joblib
import pandas as pd
import tailer
from PIL import Image
from django.shortcuts import render, redirect
from django.templatetags.static import static
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from keras.preprocessing import image as keras_image
from keras.applications.mobilenet_v2 import preprocess_input
import numpy as np
from keras.models import load_model
from pandas import DataFrame

from pages.disease_class_model.plant_disease_classification import predict
from pages.disease_file import disease_classes
from rawaProject import settings
from sklearn.preprocessing import StandardScaler


def home(request):
    return render(request, 'pages/home.html')


def sign(request):
    return render(request, 'pages/sign.html')


def back_to_home(request):
    return HttpResponseRedirect(reverse('home'))


def dashboard(request):
    data = read_last_rows(5)
    status, prob = predict_watering_probability(data)
    results = process_data(data,status, prob)
    context = {"data":results}
    return render(request, 'pages/dashboard.html',context=context)

def process_data(data,status,prob):
    # Add a new column named 'NewColumn' to the DataFrame
    data['SHOULD WATER'] = status
    data['PROBABILITY'] = prob

    data['TIME'] = data['TIME'].str.replace('Z', '')
    data[['DATE', 'TIME']] = data['TIME'].str.split('T', expand=True)

    # Convert 'Date' and 'Time' columns to datetime if needed
    # data['DATE'] = pd.to_datetime(data['DATE'])
    # data['TIME'] = pd.to_datetime(data['TIME'], format='%H:%M:%S').dt.time

    data = data.drop(['TEMPERATURE'], axis=1)
    # data = data.drop(['SHOULD WATER'], axis=1)
    data = data.drop(['SOILMOISTURE'], axis=1)
    data['TIME'] = data['TIME'].apply(lambda x: pd.to_datetime(x).strftime('%I:%M %p'))
    result_list = data.to_dict(orient='records')
    return result_list

def upload_image(request):
    if request.method == 'POST' and request.FILES.get('imageFile'):
        uploaded_image = request.FILES['imageFile']
        # Handle the uploaded image as needed (e.g., save to a folder, process, predict etc.)
        image_bytes = uploaded_image.read()
        score1, predict_class1 = check_infected_model1(image_bytes)

        # pass to model 2
        uploaded_image.seek(0)
        image_bytes = uploaded_image.read()
        # score2, predict_class2 = check_infected_model2(image_bytes)
        plant, disease = predict_class1.split("___")
        plant = plant.replace("_"," ")
        disease = disease.split(" ")
        all_disease = [d.replace("_"," ") for d in disease]
        all_disease = ",".join(all_disease)
        if "healthy" in all_disease.lower():
            all_disease = "No Disease"
        predicted_dict = {
            "model_1": {"plant": plant, "disease": all_disease}
        }
        return JsonResponse({'success': True, 'data': predicted_dict})
    else:
        return JsonResponse({'success': False, 'message': 'Image upload failed'})

def check_infected_model1(binary_image):
    model_url = static('models/plant-disease-model.pth')
    model_path = f"{os.path.join(settings.BASE_DIR, 'pages')}/{model_url}"
    return predict(binary_image, model_path, disease_classes)




def check_infected_model2(binary_image):
    class_labels = ["disease", "healthy"]
    model_url = static('models/keras_model.h5')
    model_path = f"{os.path.join(settings.BASE_DIR, 'pages')}/{model_url}"
    model = load_model(model_path)

    img = Image.open(BytesIO(binary_image))
    img = img.convert("RGB")
    img = img.resize((224, 224))

    # Convert the image to an array
    img_array = keras_image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Make predictions
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions)
    predicted_class_label = class_labels[predicted_class]
    return np.max(predictions), predicted_class_label

def predict_watering_probability(input_values):
    # load scalar as well
    sc_model_path = static('models/minmax_scaler.joblib')
    sc_model_path = f"{os.path.join(settings.BASE_DIR, 'pages')}/{sc_model_path}"

    data = input_values.drop(['TIME'], axis=1)
    data = data.drop(['SHOULD WATER'], axis=1)
    loaded_scaler = joblib.load(sc_model_path)
    scaled_features = loaded_scaler.transform(data)

    # load model
    model_path = static('models/model.h5')
    model_path = f"{os.path.join(settings.BASE_DIR, 'pages')}/{model_path}"
    loaded_model = load_model(model_path)

    # Predict probabilities
    probabilities = loaded_model.predict(scaled_features)

    # Convert probabilities to class labels
    predictions = np.where(probabilities > 0.5, 1, 0)
    predictions = predictions.reshape(-1)

    watering_status_list = []
    prob_list = []
    for pred,prob in zip(predictions,probabilities):
        watering_status = 'YES' if pred else 'NO'
        watering_status_list.append(watering_status)
        prob_list.append(round(prob[0]*100,2))

    return watering_status_list, prob_list

def read_last_rows(n_rows=5):
    # get the last 5 records and predict watering status and put it in the json:
    # Load the dataset
    import io
    file_path = static('files/ESPSS.csv')
    file_path = f"{os.path.join(settings.BASE_DIR, 'pages')}/{file_path}"

    with open(file_path) as file:
        last_lines = tailer.tail(file, 9)
    records = pd.read_csv(io.StringIO('\n'.join(last_lines)), header=None)

    records.columns = ['TIME', 'TEMPERATURE','HUMIDITY','SOILMOISTURE','SHOULD WATER']
    return records.tail(5)
