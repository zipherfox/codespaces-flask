from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow all domains to access the API

@app.route("/index")
def hello_world():
    return render_template("index.html", title="Hello")
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'message': 'Flask message'})


if __name__ == '__main__':
    app.run(debug=True,port=5000)