from eNMS.forms import BaseForm
from eNMS.fields import (
    BooleanField,
    HiddenField,
    InstanceField,
    IntegerField,
    MultipleInstanceField,
    PasswordField,
    SelectField,
    StringField,
)


class Form(BaseForm):
    form_type = HiddenField(default="custom")
    address = SelectField(choices=[("ipv4", "IPv4"), ("ipv6", "IPv6")])
    connected_links = MultipleInstanceField("Links", model="link")
    hostname = StringField("Username", default="admin")
    ip_address = StringField("IP address")
    neighbor = InstanceField("Devices", model="device")
    ports = MultipleInstanceField("Port", model="port")
    password = PasswordField("Password")
    carry_customer_traffic = BooleanField("Carry Customer Traffic", default=False)


class PanelForm(BaseForm):
    form_type = HiddenField(default="panel")
    action = "eNMS.plugins.submitPanelForm"
    ip_address = StringField("IP address", render_kw={"help": "ip_address"})
    router_id = IntegerField("Router ID")
