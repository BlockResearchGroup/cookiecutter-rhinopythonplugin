# rename the folder with the plugin name
# to a folder with the plugin name and the guid
# set the guid in the __plugin__ file

import os
import uuid

plugin_name = "{{cookiecutter.plugin_name}}"

if os.path.exists(plugin_name):
    if os.path.isdir(plugin_name):

        guid = str(uuid.uuid4())

        src = plugin_name
        dst = "{}\{{}\}".format(plugin_name, guid)

        try:
            os.rename(src, dst)

        except:
            pass

        else:
            filepath = os.path.join(dst, 'dev', '__plugin__.py')

            with open(filepath, 'r') as f:
                s = f.read()

            with open(filepath, 'w') as f:
                f.write(s.replace("id = {}", "id = \{{}\}".format(guid)))
