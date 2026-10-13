from datetime import datetime, timezone
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/health/live', methods=['GET'])
def liveness_check():
    """Перевірка життєздатності процесу застосунку (Liveness)"""
    return jsonify({
        "status": "alive",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }), 200

@app.route('/healthz/ready', methods=['GET'])
def readiness_check():
    """Перевірка готовності застосунку до обробки трафіку (Readiness)"""
    return jsonify({
        "status": "ready",
        "database": "not_connected_yet",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)