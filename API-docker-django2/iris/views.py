from django.shortcuts import render
from .models import Iris
from django.http import HttpResponse, JsonResponse
from .forms import IrisForm
from django.views.decorators.csrf import csrf_exempt
import json
import joblib
import argparse
from os import path
import numpy as np
import sys
sys.path.append('../iris')
from .train import load_data
from .utils import load_models, check_inputs

model, tf = load_models()

# Create your views here.
@csrf_exempt
def predict_test(request): # GET
    X, y = load_data()
    X_tf = tf.transform(X)
    y_hat = model.predict(X_tf)  #y_hat -> array(['iris ????'], dtype=?)

    data = {'predict_test': 'predict'}

    return JsonResponse(data)#, safe=False)

@csrf_exempt
def predict(request): # POST

    data = json.loads(request.body)

    x = list((data['features']).split(","))
    x = np.array(x).reshape(1,-1)
    print(f'x: {x}')
    y_hat = model.predict(tf.transform(x))
    print(f'y_hat: {y_hat}')
    data['label'] = str(y_hat)

    return JsonResponse(data) # json
