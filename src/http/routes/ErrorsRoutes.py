from src.http.controllers.ErrorsController import NotFoundController

errors_routes = {
    "not_found_route": 404, "not_found_controller": NotFoundController.as_view("not_found")
}
