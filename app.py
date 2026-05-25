from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import datetime
import logging
from elasticsearch import Elasticsearch

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Connect to Elasticsearch
es = Elasticsearch("http://elasticsearch:9200")

def log_to_es(level, message, endpoint):
    """Send log to Elasticsearch"""
    try:
        es.index(index="sre-app-logs", document={
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "level": level,
            "message": message,
            "endpoint": endpoint
        })
    except Exception as e:
        logger.error(f"Could not send log to Elasticsearch: {e}")

@app.route('/')
def home():
    log_to_es("INFO", "Home endpoint called", "/")
    return jsonify({"service": "sre-project-1", "status": "running"})

@app.route('/health')
def health():
    log_to_es("INFO", "Health check passed", "/health")
    return jsonify({"healthy": True, "timestamp": datetime.datetime.utcnow().isoformat()}), 200

@app.route('/info')
def info():
    log_to_es("INFO", "Info endpoint called", "/info")
    return jsonify({"app": "sre-project-1", "language": "Python"})

@app.route('/error')
def error():
    log_to_es("ERROR", "Error endpoint hit!", "/error")
    return jsonify({"error": "This is a test error"}), 500

if __name__ == '__main__':
    logger.info("Starting SRE app...")
    app.run(host='0.0.0.0', port=5000)