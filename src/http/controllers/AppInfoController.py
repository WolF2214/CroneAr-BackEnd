from flask.views import MethodView
import json, os
from dotenv import load_dotenv

load_dotenv()

class StatusController(MethodView):
    def get(self): 
        value = {
        "data":{
            "status": 200,
            "app_name": os.getenv("APP_NAME"),
            "message": "OK"
            }
        }
        return json.dumps(value)

class VersionController(MethodView):
    def get(self): 
        value = {
        "data":{
            "status": 200,
            "app_version": os.getenv("APP_VERSION")
            }
        }
        return json.dumps(value)