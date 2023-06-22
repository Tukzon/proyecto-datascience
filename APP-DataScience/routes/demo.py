from flask import Blueprint, jsonify, request
from controllers import demo

demo_bp = Blueprint('demo_bp', __name__)

@demo_bp.route('/', methods=['GET'])
def index():
    return demo.index()

@demo_bp.route('/procesar-pago', methods=['POST'])
def procesar_pago():
    return demo.procesar_pago()