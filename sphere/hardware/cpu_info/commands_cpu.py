import typer



from .cpu_info import cpu_show
from .handle_cpu_flags import handle_cpu_flags

def commands_cpu(app: typer.Typer):
    
    @app.command("cpu", help="Show CPU information -m for minimal, -f for full")
    def cpu(   
        minimal: bool = typer.Option(False, "-m", help="Show minimal CPU info"),
        full: bool = typer.Option(False, "-f", help="Show full CPU info")
        ):
        mode = handle_cpu_flags(minimal, full)
        cpu_show(mode)
        raise typer.Exit() 