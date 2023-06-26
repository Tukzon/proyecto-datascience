from flask import Blueprint, jsonify, request, render_template
from services.prod_generator import new_product

ct_demo = Blueprint('ct_demo', __name__)

def index():
    producto1 = new_product()
    producto2 = new_product()
    producto3 = new_product()
    return render_template('index.html', producto1 = producto1, producto2 = producto2, producto3 = producto3)

def procesar_pago():
    data = request.get_json()
    location = data['location']
    nombre = data['nombre']
    tarjeta = data['tarjeta']
    isFraud = data['fraudulenta']
    if isFraud:
        return False
    return True