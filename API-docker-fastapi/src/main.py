import joblib
import argparse
from os import path
import numpy as np
from train import load_data
from utils import load_models, check_inputs
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    features: list
    label: Optional[str] = None

app = FastAPI()

# load vars
model, tf = load_models()

@app.post("/predict/")
def predict(item: Item):
    x = check_inputs(item.features)
    y_hat = model.predict(tf.transform(x))
    item.label = list(y_hat)

    return item

@app.get("/")
def read_root():
    return {"Hello": "FastAPI"}
    
@app.get("/predict_test")
def predict_test():
    X, y = load_data()
    X_tf = tf.transform(X)
    y_hat = model.predict(X_tf)  #y_hat -> array(['iris ????'], dtype=?)
    return {"Predict test": "Predict"}


