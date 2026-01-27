
import subprocess
import typer

from ..get_package_manager import get_package_manager

UPDATE_COMMANDS = {
    "dnf": ["sudo", "dnf", "check-update"],
    "apt": ["sudo", "apt", "list", "--upgradable"],
    "pacman": ["sudo", "pacman", "-Qu"],
    "zypper": ["sudo", "zypper", "list-updates"]
}

def check_update():

    pkg=get_package_manager()

    manager_flags = UPDATE_COMMANDS.get(pkg, {})

    arguments = manager_flags

    result = subprocess.run(
        arguments,
        stdin=None,
        stdout=None,
        stderr=None
    )
    typer.echo(result.stdout)
    typer.echo(result.stderr)
    
