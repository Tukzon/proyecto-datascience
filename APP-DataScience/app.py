from flask import Flask,g

from routes.predictions import predictions_bp
from routes.demo import demo_bp
from services.db import create_tables

app = Flask(__name__)

app.register_blueprint(predictions_bp)
app.register_blueprint(demo_bp)

@app.teardown_appcontext
def close_db_connection(exception):
    db_connection = g.pop('db_connection', None)
    if db_connection is not None:
        db_connection.close()

if __name__ == '__main__':
    with app.app_context():
        create_tables()
        app.run(host='0.0.0.0', port=8000 ,debug=True)