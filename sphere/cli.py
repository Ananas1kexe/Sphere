import typer

from typing import List, Optional
from pathlib import Path

from sphere import app_version

import  sphere_native_rust

app = typer.Typer(help="Sphere {version} Command Line Interface".format(version=app_version.VERSION))

@app.command()
def main(
    show_version: bool = typer.Option(False, '-v', '--version'),
    show_cpu: bool = typer.Option(False, '--cpu'),
    show_ram: bool = typer.Option(False, '--ram'),
    optimize: bool = typer.Option(False, '--optimize')
):
    if show_version:
        typer.echo(app_version.VERSION)
    if show_cpu:
        typer.echo(f"CPU Count: {cpu.get_cpu_count()}")
    if show_ram:
        typer.echo(f"RAM Info: {ram.get_ram_info()}")
    if optimize:
        tasks.run_optimization()
    if not (show_version or show_cpu or show_ram or optimize):
        typer.echo("Use --help to see available options.")

if __name__ == "__main__":
    app()