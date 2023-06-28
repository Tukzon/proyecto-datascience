from flask import Blueprint, jsonify, request, render_template
from services.prod_generator import new_product
from services.datetime_generator import random_datetime
from services.db import get_db_connection
from urllib.parse import parse_qs
import pickle
import os
from datetime import datetime

ct_demo = Blueprint('ct_demo', __name__)

def index():
    producto1 = new_product()
    producto2 = new_product()
    producto3 = new_product()
    monto = producto1['precio'] + producto2['precio'] + producto3['precio']
    datetime = random_datetime()
    return render_template('index.html', producto1 = producto1, producto2 = producto2, producto3 = producto3, datetime = datetime, monto = monto)

def procesar_pago():
    with get_db_connection() as conn:
        cursor = conn.cursor()

        data = parse_qs(request.get_data().decode('utf-8'))
        location = data.get('location', [''])[0]
        nombre = data.get('nombre', [''])[0]
        tarjeta = data.get('tarjeta', [''])[0]
        datetime_str = data.get('datetime', [''])[0]
        isFraud = data.get('fraudulenta', [''])[0]
        monto = data.get('monto', [''])[0]

        datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
        year = datetime_obj.year
        month = datetime_obj.month
        day = datetime_obj.day
        hour = datetime_obj.hour
        minute = datetime_obj.minute

        if isFraud == '' or isFraud == None or isFraud == '0':
            isFraud = 0
        else:
            isFraud = 1

        try:
            cursor.execute("INSERT INTO transacciones (x_pos, y_pos, month, day, hour, minute, monto, nombre, fraudulenta) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (location, location, month, day, hour, minute, monto, nombre, isFraud))
        except Exception as e:
            return jsonify({'Error': str(e)}), 200

        if isFraud == 1:
            with open('modelo.pkl', 'rb') as file:
                modelo = pickle.load(file)
            prediccion = modelo.predict([[location, location, month, day, hour, minute]])
            resultado = prediccion[0]
            x_pos_pred = resultado[0]
            y_pos_pred = resultado[1]
            month_pred = resultado[2]
            day_pred = resultado[3]
            hour_pred = resultado[4]
            minute_pred = resultado[5]

            try:
                cursor.execute("INSERT INTO predicciones (x_pos, y_pos, month, day, hour, minute, fk_id_transaccion) VALUES (?, ?, ?, ?, ?, ?, ?)", (x_pos_pred, y_pos_pred, month_pred, day_pred, hour_pred, minute_pred, cursor.lastrowid))
            except Exception as e:
                return jsonify({'ERROR': str(e)}), 200

            conn.commit()
            return jsonify({'success': True}), 200

        conn.commit()
        return jsonify({'success': False}), 200
