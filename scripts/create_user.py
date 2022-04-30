from getpass import getpass

import click
from pony.orm import TransactionIntegrityError, commit, db_session

from app.models import User


@db_session
@click.command(help="Create new user")
@click.argument("username", type=str)
def create_user(username: str):
    password = getpass()
    hashed_password = User.hash_password(password)

    click.secho(f"Creating user '{username}'...")

    try:
        User(username=username, hashed_password=hashed_password)
        commit()
    except TransactionIntegrityError:
        click.secho(f"Username '{username}' already exists", fg="red")
        return

    click.secho(f"Success!", fg="green")


if __name__ == "__main__":
    create_user()
