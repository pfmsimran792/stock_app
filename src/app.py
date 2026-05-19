from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Stock Management App Running Successfully!"

@app.route('/stocks')
def stocks():
    return {
        "stocks": [
            {"id": 1, "name": "TCS", "qty": 100},
            {"id": 2, "name": "Infosys", "qty": 150}
        ]
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
