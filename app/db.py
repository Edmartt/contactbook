import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
                )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    connection = g.pop('db', None)

    if connection is not None:
        connection.close()

def init_db():
    cursor = get_db().cursor()

    with current_app.open_resource('schema.sql') as f:
        cursor.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Delete all data and creates new database and tables"""
    init_db()
    click.echo('Database Created')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
