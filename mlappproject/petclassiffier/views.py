import imp
from django.shortcuts import render
import tensorflow as tf
from tensorflow import keras
from .models import MLModels
import numpy as np
# Create your views here.
def home(request):
    petClassiffierFiles = MLModels.objects.filter(priority=2)[0]
    path_arch    = petClassiffierFiles.architecture.path
    path_weights = petClassiffierFiles.weights.path

    with open(path_arch) as json_file:
        json_config = json_file.read()

    model = tf.keras.models.model_from_json(json_config)
    model.load_weights(path_weights)

    if request.method =='POST':
        handle_uploaded_file(request.FILES['sentFile'])
        image = tf.keras.preprocessing.image.load_img('static/test.jpg',target_size =(150,150,3))
        input_arr = tf.keras.preprocessing.image.img_to_array(image)
        input_arr = np.array([input_arr]) # Convert single image to a batch.
        pred = tf.keras.activations.sigmoid(model.predict(input_arr))[0][0]
        caption = f'dog prob {pred}, cat prob {1-pred}'
        return render(request, 'home.html',{'caption':caption})
    else:
        return render(request, 'home.html') 


def handle_uploaded_file(f):
    with open('static/test.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)