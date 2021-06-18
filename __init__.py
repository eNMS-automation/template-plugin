from flask import request, render_template, Blueprint
from .forms import Form
from .models import Port  # noqa: F401


class Plugin:
    def __init__(self, server, controller, db, vs, env, **kwargs):
        self.register_routes(server, **kwargs)
        self._register_endpoints(controller)

    def register_routes(self, server, **kwargs):
        blueprint = Blueprint(kwargs["name"], __name__, **kwargs["blueprint"])

        @blueprint.route("/template_form")
        @server.process_requests
        def form():
            return render_template("/form.html", form=Form(request.form))

        @blueprint.route("/template_devices")
        @server.process_requests
        def devices():
            return render_template("/devices.html")

        server.register_blueprint(blueprint)

    def _register_endpoints(self, controller):
        @controller._register_endpoint
        def process_form_data(**data):
            return "127.0.0.1"
