from flask import Flask, render_template_string
import mysql.connector

app = Flask(__name__)

DB_CONFIG = {
    "host": "db",
    "user": "root",
    "password": "123456",
    "database": "empresa"
}

# Modificamos el diseño para incluir una tabla estilizada
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Aplicación Flask + Docker</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f4f7f6;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            background-color: #fff;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;
            max-width: 700px;
            width: 100%;
            margin: 20px;
        }
        h1 { color: #333; }
        .status { margin: 1rem 0; padding: 0.5rem; border-radius: 5px; }
        .success { background-color: #d4edda; color: #155724; }
        .error { background-color: #f8d7da; color: #721c24; }
        
        /* Estilos para la tabla de datos */
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 1.5rem;
        }
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        th {
            background-color: #007bff;
            color: white;
        }
        tr:hover { background-color: #f5f5f5; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Flask con Docker</h1>

        {% if error %}
            <div class="status error">
                <strong>Error:</strong> {{ error }}
            </div>
        {% else %}
            <div class="status success">
                <strong>Conexión exitosa a MySQL</strong>
            </div>

            <h3>Listado de Personal</h3>
            <table>
                <thead>
                    <tr>
                        <th>ID Empleado</th>
                        <th>Nombre</th>
                        <th>Apellido</th>
                        <th>Cargo</th>
                    </tr>
                </thead>
                <tbody>
                    {% for dato in datos %}
                        <tr>
                            <td>{{ dato[0] }}</td>
                            <td>{{ dato[1] }}</td>
                            <td>{{ dato[2] }}</td>
                            <td>{{ dato[3] }}</td>
                        </tr>
                    {% endfor %}
                </tbody>
            </table>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/")
def inicio():
    datos = []
    error = None
    try:
        con = mysql.connector.connect(**DB_CONFIG)
        cursor = con.cursor()
        # Pedimos las columnas específicas en orden
        cursor.execute("SELECT id_empleado, nombre, apellido, cargo FROM datos")
        datos = cursor.fetchall()
        cursor.close()
        con.close()
    except mysql.connector.Error as e:
        error = str(e)

    return render_template_string(HTML_TEMPLATE, datos=datos, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)