from flask import Flask, request

from .model import db
from .model_dao import get_compound, get_all_compounds, add_or_update_compound

app = Flask(__name__)


app.config.from_object("compounds.config.Config")
db.init_app(app)


@app.route("/compounds", methods=["GET", "POST"])
def compounds():
    if request.method == "GET":
        return get_all_compounds
    if request.method == "POST":
        return add_or_update_compound(request.form)


@app.route("/compounds/<compound>", methods=["GET"])
def compound_by_title(compound):
    return get_compound(compound)
