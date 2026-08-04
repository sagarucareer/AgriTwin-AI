from flask import Flask

from routes.disease import disease_bp
from routes.stress import stress_bp
from routes.forecast import forecast_bp
from routes.irrigation import irrigation_bp
from routes.dashboard import dashboard_bp

app = Flask(__name__)

app.register_blueprint(disease_bp)
app.register_blueprint(stress_bp)
app.register_blueprint(forecast_bp)
app.register_blueprint(irrigation_bp)
app.register_blueprint(dashboard_bp)


@app.route("/")
def home():
    return "AgriTwin-AI Backend is Running!"


if __name__ == "__main__":
    app.run(debug=True)