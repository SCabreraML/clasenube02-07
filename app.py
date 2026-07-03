from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def inicio():
    return "<h1>Flask con Docker funcionando</h1>"


@app.route("/conexion")
def conexion():
    try:
        con = mysql.connector.connect(
            host="db",
            user="root",
            password="123456",
            database="empresa"
        )

        con.close()

        return "<h2>Conexión exitosa a MySQL</h2>"

    except mysql.connector.Error as e:
        return f"<h2>Error:</h2><p>{e}</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)