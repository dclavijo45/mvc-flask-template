from controllers.api import ApiController

api_v1 = {
    "api": "/api/v1/",
    "api_controller": ApiController.as_view("api"),
    # ----------------------------------------------------------------
}