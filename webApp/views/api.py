from flask import Blueprint, json, render_template, request, jsonify
import random
from flask.helpers import make_response
from flask_restful import Api, Resource, url_for
from marshmallow import Schema, fields

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


#import saved ML model and vector
import pickle
nb_file = './webApp/views/Count_model.sav'
nb_classifier = pickle.load(open(nb_file, 'rb'))
vector_file = './webApp/views/count_vector.sav'
vector = pickle.load(open(vector_file, 'rb'))

class ml_schema(Schema):
    text = fields.Str(required=True)

schema = ml_schema()

class MLAPI(Resource):

    def get(self):
        parser = request.args
        text = parser['text']
        text = text.lower().replace('[^a-zA-Z\s\@]', '')
        vectored_new = vector.transform([text])
        pred = nb_classifier.predict(vectored_new)
        prob = nb_classifier.predict_proba(vectored_new)

        p_prob = nb_classifier.predict_proba(vectored_new)[0]
        print(f"I expect, with {max(p_prob)*100:.2f}% certainty, that this is should be {'an Incident' if pred == ['IR'] else 'a Request'}\n")

        print(f"predication made: {pred}")
        print({f"Prob: {p_prob}"})
        response = make_response(jsonify(
            {'prediction':str(pred[0]),
            'probability': f"{max(p_prob)*100:.2f}%"}


        ))

        return response

api.add_resource(MLAPI, '/v1.0/ml/', endpoint='ml')