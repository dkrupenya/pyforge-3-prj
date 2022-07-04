import click
import requests
import logging

logging.basicConfig(filename='logs/cli.log', filemode='a', level=logging.DEBUG)


@click.group()
def cli():
    pass


@click.command()
@click.option('--compound', prompt='Compound')
def get_compound(compound):
    click.echo(f'Request compound: {compound}')
    resp = requests.get(f'http://localhost:5000/compounds/{compound}')

    if resp.status_code == 404:
        click.echo('Not Found')
        return

    if resp.status_code != 200:
        logging.error(f'error: {resp}')
        click.echo('Unexpected error')
        return

    c = resp.json()
    logging.info(f'found compound: {c}')
    if c is not None:
        print_compounds([c])
        return
    else:
        click.echo('Not Found')
        return


@click.command()
def get_all():
    click.echo('Print')
    resp = requests.get(f'http://localhost:5000/compounds')
    print_compounds(resp.json())


def print_compounds(lst):
    click.echo(
        '| compound |          name |       formula |          inchi|'
        '        smiles | cross_links |         create_date |')
    click.echo(
        '|----------+---------------+---------------+---------------+'
        '---------------+-------------+---------------------|')
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
            date_created=to_str(c['date_created'], 19),
        ))


def to_str(val, length=13):
    s = str(val)
    if len(s) > length:
        return f'{s[:length - 3]}...'
    return s


cli.add_command(get_compound)
cli.add_command(get_all)

if __name__ == '__main__':
    cli()
