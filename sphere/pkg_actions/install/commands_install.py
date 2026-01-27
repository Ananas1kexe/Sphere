import typer



from .install_main import install

def commands_install(app: typer.Typer):
    
    @app.command("install", help="Install packages ")
    def install(package: str):
        install(package)
        raise typer.Exit()