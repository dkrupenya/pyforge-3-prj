import click
import requests


@click.group()
def cli():
    pass


@click.command()
@click.option('--compound', prompt='Compound')
def add_compound(compound):
    click.echo(f'Compound: {compound}')
    r = requests.get(f'http://localhost:5000/compounds/{compound}')
    c = r.json()
    if c is not None:
        print_compounds([c])
        return

    from_api = requests.get(f'https://www.ebi.ac.uk/pdbe/graph-api/compound/summary/{compound}')
    c = from_api.json()
    new_compound = c and c[compound] and c[compound][0]
    if new_compound is None:
        click.echo('Not Found')
        return

    formatted = dict(
        compound=compound,
        name=new_compound['name'],
        formula=new_compound['formula'],
        inchi=new_compound['inchi'],
        inchi_key=new_compound['inchi_key'],
        smiles=new_compound['smiles'],
        cross_links_count=len(new_compound['cross_links']),
    )
    resp = requests.post('http://localhost:5000/compounds', formatted)
    print_compounds(resp.json())


@click.command()
def get_all():
    click.echo('Print')
    resp = requests.get(f'http://localhost:5000/compounds')
    print_compounds(resp.json())


def print_compounds(lst):
    click.echo(
        '| compound |          name |       formula |          inchi|        smiles | cross_links | create_date |')
    click.echo(
        '|----------+---------------+---------------+---------------+---------------+-------------+-------------|')
    format_str = \
        '| {compound:>8} | {name:>13} | {formula:>13} | {inchi:>13} |' \
        ' {smiles:>13} | {cross_links_count:>11} | {date_created:>11} |'
    for c in lst:
        click.echo(format_str.format(
            compound=to_str(c['compound'], 8),
            name=to_str(c['name']),
            formula=to_str(c['formula']),
            inchi=to_str(c['inchi']),
            smiles=to_str(c['smiles']),
            cross_links_count=to_str(c['cross_links_count'], 11),
            date_created=to_str(c['date_created'], 11),
        ))


def to_str(val, length=13):
    s = str(val)
    if len(s) > length:
        return f'{s[:length - 3]}...'
    return s

cli.add_command(add_compound)
cli.add_command(get_all)

if __name__ == '__main__':
    cli()
