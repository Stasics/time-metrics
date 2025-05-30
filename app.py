from flask import Flask, jsonify
import time

app = Flask(__name__)
time_requests = 0

@app.route('/time')
def get_time():
    global time_requests
    time_requests += 1
    return jsonify({"time": int(time.time())})

@app.route('/metrics')
def get_metrics():
    return jsonify({"count": time_requests})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
