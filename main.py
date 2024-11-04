from flask import Flask
from routes.home import home_route
from routes.cliente import cliente_route
from models.table import db, Cliente

app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(cliente_route, url_prefix="/clientes")

if __name__ == "__main__":
    db.connect()
    db.create_tables([ Cliente ])
    app.run(debug=True)