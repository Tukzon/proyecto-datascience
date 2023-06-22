from flask import Blueprint, jsonify, request
from controllers import predictions

predictions_bp = Blueprint('predictions_bp', __name__)

@predictions_bp.route('/predict', methods=['GET'])
def predict():
    return predictions.predict()

@predictions_bp.route('/datos', methods=['GET'])
def datos():
    return predictions.datos()