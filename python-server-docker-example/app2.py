from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Docker compose with custom port 4050"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 4050))
    app.run(debug=True,host='0.0.0.0',port=port)
