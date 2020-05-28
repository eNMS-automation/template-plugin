from sqlalchemy import Boolean, Integer

from eNMS.database import db
from eNMS.models.base import AbstractBase


class Port(AbstractBase):
    __tablename__ = type = "port"
    id = db.Column(Integer, primary_key=True)
    name = db.Column(db.SmallString, unique=True)
    active = db.Column(Boolean, default=False)
