from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import sciptcontext as sc


__commandname__ = "{{cookiecutter.plugin_name}}_init"


def RunCommand(is_interactive):
    sc.sticky["{{cookiecutter.plugin_name}}"] = {}


# ==============================================================================
# Main
# ==============================================================================

if __name__ == '__main__':

    RunCommand(True)
