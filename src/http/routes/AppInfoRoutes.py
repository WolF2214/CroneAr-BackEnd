from flask import Blueprint
from src.http.controllers.AppInfoController import StatusController, VersionController

app_info = Blueprint('app_info', __name__, url_prefix='/')

app_info_routes = {
    "status_route": "/status", "status_controller": StatusController.as_view("status"),
    "version_route": "/version", "version_controller": VersionController.as_view("version")
}

app_info.add_url_rule(app_info_routes["status_route"], view_func=app_info_routes["status_controller"])
app_info.add_url_rule(app_info_routes["version_route"], view_func=app_info_routes["version_controller"])