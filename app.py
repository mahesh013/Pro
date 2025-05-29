from flask import Flask, render_template, request, jsonify
from chat import get_response

app = Flask(__name__)

@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    data = request.get_json() or {}
    text = data.get("message", "").strip()
    if not text:
        return jsonify({"answer": "Please say something!"})
    answer = get_response(text)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
