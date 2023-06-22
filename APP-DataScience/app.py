from flask import Flask

from routes.predictions import predictions_bp
from routes.demo import demo_bp

app = Flask(__name__)

app.register_blueprint(predictions_bp)
app.register_blueprint(demo_bp)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000 ,debug=True)