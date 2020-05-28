from flask import request, render_template, Blueprint
from sqlalchemy.orm import configure_mappers
from .forms import Form
from .models import Port


class Plugin:
    def __init__(self, server, controller, db, **kwargs):
        self.register_routes(server, **kwargs)
        self.register_endpoints(controller)
        self.create_ports(db)

    def register_routes(self, server, **kwargs):
        blueprint = Blueprint(f"{__name__}_bp", __name__, **kwargs["blueprint"])

        @blueprint.route("/form")
        def plugin():
            return render_template("/form.html", form=Form(request.form))

        server.register_blueprint(blueprint, url_prefix=kwargs["url_prefix"])

    def register_endpoints(self, controller):
        @controller.register_endpoint
        def process_form_data(**data):
            return int(data["router_id"] or 0) * 2

    def create_ports(self, db):
        db.base.metadata.create_all(bind=db.engine)
        configure_mappers()
        for index in range(10):
            db.factory("port", name=f"port{index}")
        db.session.commit()
