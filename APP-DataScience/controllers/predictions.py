from flask import Blueprint, jsonify, request, render_template
from services.db import get_db_connection

ct_predictions = Blueprint('ct_predictions', __name__)

def predict():
    return render_template('predict.html')

def datos():
    with get_db_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM transacciones ORDER BY id DESC""")
        rows = cursor.fetchall()
        datos = []
        for row in rows:
            row_dict = {}
            for i, col_name in enumerate(cursor.description):
                row_dict[col_name[0]] = row[i]
            datos.append(row_dict)

    return render_template('datos.html', datos = datos)