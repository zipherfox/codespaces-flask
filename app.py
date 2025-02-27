from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_cors import CORS
from google import genai

app = Flask(__name__)
CORS(app)  # Allow all domains to access the API


@app.route("/index")
def hello_world():
    return render_template("index.html", title="Hello")


@app.route("/api", methods=["GET"])
def get_api():
    return render_template("api.html", title="API")


@app.route("/api/test", methods=["GET"])
def get_data():
    return jsonify({"message": "Flask message"})


@app.route("/api/ai_test", methods=["GET"])
def get_gemini():
    client = genai.Client(api_key="AIzaSyBCRspa9S8DCXQwlVbccjOYS5zUJtqOA-M")
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="Explain how AI works",
    )
    print(response.text)
    return jsonify({"AI_Response": response.text})


@app.route("/api/data", methods=["POST"])
def submit_data():
    data = request.get_json()
    print(data)
    client = genai.Client(api_key="AIzaSyBCRspa9S8DCXQwlVbccjOYS5zUJtqOA-M")
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=data["data"],
    )
    print(response.text)
    return jsonify


@app.route("/feedback")
def feedback():
    data = request.args.get("data")
    return render_template("feedback.html", data=data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
