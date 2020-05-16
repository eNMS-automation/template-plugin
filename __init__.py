from flask import request, render_template, Blueprint
from .forms import Form


class Plugin:
    def __init__(self, server, controller, **kwargs):
        self.register_routes(server, **kwargs)
        self.register_endpoints(controller)

    def register_routes(self, server, **kwargs):
        blueprint = Blueprint(f"{__name__}_bp", __name__, **kwargs["blueprint"])

        @blueprint.route("/form")
        def plugin():
            return render_template("/form.html", form=Form(request.form))

        server.register_blueprint(blueprint, url_prefix=kwargs["url_prefix"])

    def register_endpoints(self, controller):
        @controller.register_endpoint
        def process_form_data(**data):
            return int(data.get("router_id", 10)) * 2
