from flask import Flask, request, jsonify

from .model import db
from .model_dao import get_compound, get_all_compounds, add_or_update_compound

app = Flask(__name__)


app.config.from_object("compounds.config.Config")
db.init_app(app)


@app.route("/compounds", methods=["GET", "POST"])
def compounds():
    if request.method == "GET":
        return jsonify(get_all_compounds()), 200
    if request.method == "POST":
        return jsonify(add_or_update_compound(request.form)), 200


@app.route("/compounds/<compound>", methods=["GET"])
def compound_by_title(compound):
    return jsonify(get_compound(compound)), 200
