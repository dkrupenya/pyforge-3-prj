from flask import Flask, request, jsonify
import requests
import logging

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
    cached_compound = get_compound(compound)
    if cached_compound is not None:
        return jsonify(get_compound(compound)), 200

    resp = requests.get(f'https://www.ebi.ac.uk/pdbe/graph-api/compound/summary/{compound}')
    c = resp.json()
    api_compound = c and c[compound] and c[compound][0]
    logging.info(f'get compound from api: {api_compound}')
    if api_compound is None:
        return jsonify(None), 404

    formatted = dict(
        compound=compound,
        name=api_compound['name'],
        formula=api_compound['formula'],
        inchi=api_compound['inchi'],
        inchi_key=api_compound['inchi_key'],
        smiles=api_compound['smiles'],
        cross_links_count=len(api_compound['cross_links']),
    )
    return jsonify(add_or_update_compound(formatted)), 200
