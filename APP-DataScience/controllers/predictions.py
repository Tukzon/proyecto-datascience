from flask import Blueprint, jsonify, request, render_template
from services.db import get_db_connection

ct_predictions = Blueprint('ct_predictions', __name__)

def predict():
    return render_template('predict.html')

def datos():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM transacciones ORDER BY id DESC""")
    rows = cursor.fetchall()
    datos = [dict(row) for row in rows]
    conn.close()
    return render_template('datos.html', datos = datos)