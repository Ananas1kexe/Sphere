import subprocess
import typer

from typing import Optional
from dataclasses import dataclass

from ..get_package_manager import get_package_manager
from .flag_manager import flag_update_manager
@dataclass
class Update:
    sudo: str = "sudo"
    pkg: Optional[str] = None
    update: str = "update"


def update_main(
        flag1: bool,
        flag2: bool,
):

    u = Update(pkg=get_package_manager())

    list = flag_update_manager(u.pkg,flag1,flag2)

    arguments = [u.sudo, u.pkg, u.update] + list

    result = subprocess.run(
        arguments,
        stdin=None,
        stdout=None,
        stderr=None
    )
    typer.echo(result.stdout)
    typer.echo(result.stderr)
    
