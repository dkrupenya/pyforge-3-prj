from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Compound(db.Model):
    __tablename__ = "compounds"

    id = db.Column(db.Integer, primary_key=True)
    compound = db.Column(db.String(), unique=True)
    name = db.Column(db.String(), nullable=True)
    formula = db.Column(db.String(), nullable=True)
    inchi = db.Column(db.String(), nullable=True)
    inchi_key = db.Column(db.String(), nullable=True)
    smiles = db.Column(db.String(), nullable=True)
    cross_links_count = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)
    date_updated = db.Column(db.DateTime, nullable=False)

    def __init__(self, compound, name, formula, inchi, inchi_key, smiles, cross_links_count=0):
        self.compound = compound
        self.name = name
        self.formula = formula
        self.inchi = inchi
        self.inchi_key = inchi_key
        self.smiles = smiles
        self.cross_links_count = cross_links_count
        self.date_created = datetime.now()
        self.date_updated = datetime.now()

    def __repr__(self):
        return f"{self.compound}, {self.name}, {self.smiles}"

    def to_json(self) -> dict:
        return dict(
            compound=self.compound,
            name=self.name,
            formula=self.formula,
            inchi=self.inchi,
            inchi_key=self.inchi_key,
            smiles=self.smiles,
            cross_links_count=self.cross_links_count,
            date_created=self.date_created,
            date_updated=self.date_updated,
        )
