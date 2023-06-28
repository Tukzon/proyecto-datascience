from flask import Blueprint, jsonify, request
from controllers import predictions

predictions_bp = Blueprint('predictions_bp', __name__)

@predictions_bp.route('/datos-predict', methods=['GET'])
def predict():
    #Aquí van las predicciones
    return predictions.datos_predict()

@predictions_bp.route('/datos', methods=['GET'])
def datos():
    #Aquí van todas las transacciones registradas con el form de /procesar-pago
    return predictions.datos()

@predictions_bp.route('/show', methods=['GET'])
def show():
    return predictions.show()