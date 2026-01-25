import subprocess
import typer

def update_main():
    result = subprocess.run(
        ["sudo", "dnf", "update"],
        stdin=None,
        stdout=None,
        stderr=None
    )
    typer.echo(result.stdout)
    typer.echo(result.stderr)
    
