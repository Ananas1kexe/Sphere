import typer

from typing import List, Optional
from pathlib import Path

import app_version

app = typer.Typer(help="Hello")

@app.command()
def main(show_version: bool = typer.Option(False, '-v', '--version', help="Show application version")):
    if show_version:
        typer.echo(app_version.VERSION)
        raise typer.Exit()



if __name__ == "__main__":
    app()