from flask import Flask
from .ui.routes import ui_bp

def create_app():
    app=Flask(__name__)

    app.register_blueprint(ui_bp)


    return app