from flask import Blueprint, jsonify, request, render_template
from services.prod_generator import new_product
from services.datetime_generator import random_datetime
from services.db import get_db_connection
from urllib.parse import parse_qs
import pickle
import os

ct_demo = Blueprint('ct_demo', __name__)

def index():
    producto1 = new_product()
    producto2 = new_product()
    producto3 = new_product()
    monto = producto1['precio'] + producto2['precio'] + producto3['precio']
    datetime = random_datetime()
    return render_template('index.html', producto1 = producto1, producto2 = producto2, producto3 = producto3, datetime = datetime, monto = monto)

def procesar_pago():
    conn = get_db_connection()
    cursor = conn.cursor()
    # Obtener los datos del cuerpo de la solicitud en formato URL codificado
    data = parse_qs(request.get_data().decode('utf-8'))

    # Acceder a los valores de los campos del formulario
    location = data.get('location', [''])[0]
    nombre = data.get('nombre', [''])[0]
    tarjeta = data.get('tarjeta', [''])[0]
    datetime = data.get('datetime', [''])[0]
    isFraud = data.get('fraudulenta', [''])[0]
    monto = data.get('monto', [''])[0]
    cursor.execute("""INSERT INTO transacciones (x_pos, y_pos, month, day, hour, minute, monto, nombre, fraudulenta) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", (location, location, datetime, datetime, datetime, datetime, monto, nombre, isFraud))
    if int(isFraud) == 1:
        #Se debe hacer la predicción e insertarla en la base de datos
        with open('modelo.pkl', 'rb') as file:
            modelo = pickle.load(file)
        prediccion = modelo.predict([[location, location, datetime, datetime, datetime, datetime]])
        resultado = prediccion[0]
        x_pos_pred = resultado[0]
        y_pos_pred = resultado[1]
        month_pred = resultado[2]
        day_pred = resultado[3]
        hour_pred = resultado[4]
        minute_pred = resultado[5]
        cursor.execute("""INSERT INTO predicciones (x_pos, y_pos, month, day, hour, minute, fk_id_transaccion) VALUES (?, ?, ?, ?, ?, ?, ?)""", (x_pos_pred, y_pos_pred, month_pred, day_pred, hour_pred, minute_pred, cursor.lastrowid))
        conn.commit()
        conn.close()
        return jsonify({'success': True}), 200
    conn.commit()
    conn.close()
    return jsonify({'success': False}), 200