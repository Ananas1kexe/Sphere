import typer



from .disk_info import disk_show
from .handle_disk_flags import handle_disk_flags
def commands_disk(app: typer.Typer):
    
    @app.command("disk", help="Show Disk information -m for minimal, -f for full")
    def disk(   
        minimal: bool = typer.Option(False, "-m", help="Show minimal Disk info"),
        full: bool = typer.Option(False, "-f", help="Show full Disk info")
        ):
        mode = handle_disk_flags(minimal, full)
        disk_show(mode)
        raise typer.Exit() 