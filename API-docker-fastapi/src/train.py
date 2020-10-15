import argparse
from os import path, mkdir, makedirs, umask
import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline, Pipeline

import joblib

DIR_NAME = path.dirname(__file__)

def load_data():
    df_data = pd.read_csv('iris.data')
    #pd.read_csv(path.join('..','data', 'iris.data'))

    X = df_data.iloc[:,:4].values
    y = df_data.iloc[:,4].values

    return X, y

def transform(X):
    tf = StandardScaler().fit(X)

    pipe = Pipeline(
        [
            ('standard_scaler', tf)
        ]
    )
    #return tf
    return pipe

def train(args):
    X,y = load_data()

    # transformation
    tf = transform(X)

    clf = MLPClassifier(max_iter=2000)

    X_tf = tf.transform(X)
    clf.fit(X_tf,y)
    print(X_tf.shape)
    clf.predict(X)

    #save
    dump_folder=path.join(args['output_folder'],args['experiment_name'])
    print(dump_folder)
    if not path.exists(dump_folder):
        makedirs(dump_folder)

    # dump model
    filename = 'model_mlp_{}_v0.1.pkl'.format(args['model_name_tag'])
    #joblib.dump(clf,filename=dump_folder+'/classifier')
    joblib.dump(clf,filename=path.join(dump_folder,filename))

    # dump normalization
    filename = 'tf_std_{}_v0.1.pkl'.format(args['model_name_tag'])
    joblib.dump(tf,filename=path.join(dump_folder,filename))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Iris classifier training 0.0.1')
    parser.add_argument('--experiment_name', required=True, type=str)
    parser.add_argument('--output_folder', default=path.join(DIR_NAME, 'models'), type=str)
    parser.add_argument('--model_name_tag', required=True, type=str)
    args = vars(parser.parse_args())

    train(args)