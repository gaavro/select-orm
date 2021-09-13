from flask import Flask, current_app
from app.models.grupo_um_model import GrupoUmModel
from app.models.grupo_dois_model import GrupoDoisModel
from flask.cli import AppGroup
import click
from faker import Faker

fake = Faker()


def cli_grupos(app:Flask):
    cli = AppGroup('cli_grupos')
    @cli.command('create')
    @click.argument('amount')
    def cli_grupos_create(amount):
        session = current_app.db.session
        for _ in range(int(amount)):
            pessoa = GrupoUmModel(nome=fake.name(), idade=fake.random_int(min=18, max=28))
            session.add(pessoa)
            GrupoDoisModel(nome=fake.name(), idade=fake.random_int(min=18, max=28), conjuge=pessoa)
        session.commit()
    app.cli.add_command(cli)



def init_app(app:Flask):
    cli_grupos(app)