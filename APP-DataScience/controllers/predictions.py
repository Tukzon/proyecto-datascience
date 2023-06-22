from flask import Blueprint, jsonify, request, render_template

ct_predictions = Blueprint('ct_predictions', __name__)

def predict():
    return render_template('predict.html')

def datos():
    return render_template('datos.html', datos = 'AQUI VAN LOS DATOS')