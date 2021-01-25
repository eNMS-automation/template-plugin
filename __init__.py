from flask import request, render_template, Blueprint
from .forms import Form
from .models import Port  # noqa: F401


class Plugin:
    def __init__(self, server, controller, db, **kwargs):
        self.register_routes(server, **kwargs)
        self.register_endpoints(controller)

    def register_routes(self, server, **kwargs):
        blueprint = Blueprint(f"{__name__}_bp", __name__, **kwargs["blueprint"])

        @blueprint.route("/template_form")
        @server.monitor_requests
        def form():
            return render_template("/form.html", form=Form(request.form))

        @blueprint.route("/template_devices")
        @server.monitor_requests
        def devices():
            return render_template("/devices.html")

        server.register_blueprint(blueprint)

    def register_endpoints(self, controller):
        @controller.register_endpoint
        def process_form_data(**data):
            return "127.0.0.1"
