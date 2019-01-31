from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import sciptcontext as sc
import clr

clr.AddReference("Eto")
clr.AddReference("Rhino.UI")

import Rhino
from compas_rhino.etoforms import SettingsForm


__commandname__ = "{{cookiecutter.plugin_name}}_init"


def RunCommand(is_interactive):
    if "{{cookiecutter.plugin_name}}" not in sc.sticky:
        raise Exception("Initialise the plugin first!")

    settings = sc.sticky["{{cookiecutter.plugin_name}}"]

    dialog = SettingsForm(settings)

    if dialog.ShowModal(Rhino.UI.RhinoEtoApp.MainWindow):
        settings.update(dialog.settings)


# ==============================================================================
# Main
# ==============================================================================

if __name__ == '__main__':

    RunCommand(True)
