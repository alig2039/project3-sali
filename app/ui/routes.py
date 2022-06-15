from flask import Blueprint, render_template, request


ui_bp = Blueprint("ui", __name__, template_folder='./templates',
                  static_folder='./static', static_url_path='/static')


@ui_bp.route('/', methods=['GET', 'POST'])
def index():
    """
    This renders the UI

    """
    if request.method == "POST":
        print(request.form)
    return render_template("index.html")
