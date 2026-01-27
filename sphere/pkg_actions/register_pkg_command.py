
from .update.commands_update import commands_update
from .install.commands_install import commands_install


def register_pkg_commands(app):
    commands_update(app)
    commands_install(app)