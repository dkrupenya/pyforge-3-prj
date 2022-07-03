from datetime import datetime
from typing import Optional, List

from .model import db, Compound


def _get_compound(compound: str) -> Optional[Compound]:
    res = Compound.query.filter(Compound.compound == compound)
    return res


def get_compound(compound: str) -> Optional[dict]:
    res = _get_compound(compound)
    if res is not None:
        return res.to_json()
    return None


def get_all_compounds() -> List[dict]:
    res = Compound.query.all()
    return list(map(Compound.to_json, res))


def add_or_update_compound(compound: dict) -> dict:
    existing_compound = _get_compound(compound['compound'])
    if existing_compound is not None:
        existing_compound.compound = compound['compound'],
        existing_compound.name = compound['name'],
        existing_compound.formula = compound['formula'],
        existing_compound.inchi = compound['inchi'],
        existing_compound.inchi_key = compound['inchi_key'],
        existing_compound.smiles = compound['smiles'],
        existing_compound.cross_links_count = compound['cross_links_count']
        existing_compound.existing_compound = datetime.now()
        db.session.commit()
        return existing_compound.to_json()
    else:
        new_compound = Compound(
            compound=compound['compound'],
            name=compound['name'],
            formula=compound['formula'],
            inchi=compound['inchi'],
            inchi_key=compound['inchi_key'],
            smiles=compound['smiles'],
            cross_links_count=compound['cross_links_count']
        )
        db.session.add(new_compound)
        db.session.commit()
        return new_compound.to_json()

