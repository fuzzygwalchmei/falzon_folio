from flask import Blueprint, json, render_template, request, jsonify
import random
from flask.helpers import make_response
from flask_restful import Api, Resource, url_for
from marshmallow import Schema, fields

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


#import saved ML model and vector
import pickle
nb_file = './webApp/views/Tfidf_model.sav'
nb_classifier = pickle.load(open(nb_file, 'rb'))
tfidf_file = './webApp/views/tfidf_vector.sav'
tfidf = pickle.load(open(tfidf_file, 'rb'))

class ml_schema(Schema):
    text = fields.Str(required=True)

schema = ml_schema()

class MLAPI(Resource):

    def get(self):
        parser = request.args
        text = parser['text']
        text = text.lower().replace('[^a-zA-Z\s\@]', '')
        tfidf_new = tfidf.transform([text])
        pred = nb_classifier.predict(tfidf_new)
        prob = nb_classifier.predict_proba(tfidf_new)
        print(f"predication made: {pred}")
        print({f"Prob: {prob}"})
        response = make_response(jsonify(
            {'prediction':str(pred[0]),
            'probability': str(prob)}


        ))

        return response

api.add_resource(MLAPI, '/v1.0/ml/', endpoint='ml')