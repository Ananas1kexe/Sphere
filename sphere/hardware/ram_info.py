import typer
import psutil


def to_gb(bytes: int):
    return f"{bytes / (1024 ** 3):.2f} GB"

def ram_show():
    ram = psutil.virtual_memory()
    typer.echo()
    typer.echo(typer.style("RAM Information:", fg=typer.colors.GREEN, bold=True))

    typer.echo(f"Total:     {to_gb(ram.total)}")
    typer.echo(f"Used:      {to_gb(ram.used)}")
    typer.echo(f"Available: {to_gb(ram.available)}")
    typer.echo(f"Free:      {to_gb(ram.free)}")
    typer.echo(f"Usage:     {ram.percent}%")