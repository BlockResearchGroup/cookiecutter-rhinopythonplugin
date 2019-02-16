# rename the folder with the plugin name
# to a folder with the plugin name and the guid
# set the guid in the __plugin__ file

import os
import uuid

plugin_name = "{{cookiecutter.plugin_name}}"
plugin_src = os.getcwd()

if os.path.exists(plugin_src):
    if os.path.isdir(plugin_src):

        guid = str(uuid.uuid4())

        plugin_dst = plugin_src + "{" + guid + "}"

        try:
            os.rename(plugin_src, plugin_dst)

        except:
            pass

        else:
            filepath = os.path.join(plugin_dst, 'dev', '__plugin__.py')

            with open(filepath, 'r') as f:
                s = f.read()

            with open(filepath, 'w') as f:
                search = 'id = ""'
                replace = 'id = ' + '"{' + guid + '}"'
                f.write(s.replace(search, replace))
