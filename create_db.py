from app.ui.utils import db
from app.ui.database import Record
from main import app

with app.app_context():
    db.create_all()
