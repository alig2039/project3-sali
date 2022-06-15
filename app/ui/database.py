from .utils import db
from datetime import datetime


class Record(db.Model):
    __tablename__ = "records"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer())
    occupation = db.Column(db.String(23), nullable=False)
    vaccination_status = db.Column(db.String(5), nullable=False)
    vaccination_date = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return self.name
