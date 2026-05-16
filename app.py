from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import datetime

# Create the Flask app
app = Flask(__name__)

# This one line adds a /metrics endpoint automatically
# Prometheus will scrape this to collect data about your app
metrics = PrometheusMetrics(app)


# --- Routes (API endpoints) ---

@app.route('/')
def home():
    """Main endpoint — just returns app info"""
    return jsonify({
        "service": "sre-project-1",
        "status": "running",
        "version": "1.0.0"
    })


@app.route('/health')
def health():
    """
    Health check endpoint.
    SRE tools (Kubernetes, load balancers) call this to check if the app is alive.
    Always return 200 if healthy, 500 if not.
    """
    return jsonify({
        "healthy": True,
        "timestamp": datetime.datetime.utcnow().isoformat()
    }), 200


@app.route('/info')
def info():
    """Returns some system info — useful for debugging in production"""
    return jsonify({
        "app": "sre-project-1",
        "language": "Python",
        "framework": "Flask",
        "description": "My first SRE containerised app"
    })


# Start the app
if __name__ == '__main__':
    # host='0.0.0.0' means "accept connections from anywhere"
    # (not just localhost) — required inside a Docker container
    app.run(host='0.0.0.0', port=5000, debug=False)
