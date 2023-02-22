from flask import Flask
from src.http.routes.ErrorsRoutes import *
from src.http.routes.AppInfoRoutes import app_info

app = Flask(__name__)
app.register_blueprint(app_info)

# Ruta del error 404
app.register_error_handler(errors_routes["not_found_route"], errors_routes["not_found_controller"])

