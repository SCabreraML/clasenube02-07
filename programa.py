from flask import Flask

app = Flask(__name__)
@app.route("/")
def inicio():
    return """
    <h1>Mi primera aplicación creada con docker</h1>
    <h2>Creada por Sebastián</h2>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)