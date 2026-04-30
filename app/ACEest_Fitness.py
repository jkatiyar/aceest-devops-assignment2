from flask import Flask, jsonify

app = Flask(__name__)

# -------------------------
# Version 2 Home Endpoint
# -------------------------
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to ACEest Fitness API - Version 2 🚀",
        "version": "v2",
        "status": "Running",
        "features": [
            "Member Management",
            "Plan Tracking",
            "API Versioning"
        ]
    })


# -------------------------
# Health Check Endpoint
# -------------------------
@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "version": "v2"
    })


# -------------------------
# Run App
# -------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)