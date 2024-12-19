from flask import Flask
from db import DATABASE_URL
from db import db  # Importar db desde database.py
from routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL  # Establecer la cadena de conexión directamente en la configuración
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)  # Inicializar la base de datos con la app
    register_routes(app)  # Registrar las rutas
    return app

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, port=2000)