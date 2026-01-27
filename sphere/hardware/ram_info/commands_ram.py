import typer

from .ram_info import ram_show
from .handle_ram_flags import handle_ram_flags

def commands_ram(app: typer.Typer):
    
    @app.command("ram", help="Show RAM information -m for minimal, -f for full")
    def ram(
        minimal: bool = typer.Option(False, "-m", help="Show minimal RAM info"),
        full: bool = typer.Option(False, "-f", help="Show full RAM info")
        ):
        mode = handle_ram_flags(minimal, full)
        ram_show(mode)
        raise typer.Exit()