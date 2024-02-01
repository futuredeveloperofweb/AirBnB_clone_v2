#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the contents of
# the web_static folder of your AirBnB Clone repo, using the
# function do_pack
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    All files in the folder web_static must be added to the final
    archive

    Returns:
        the archive path if the archive has been correctly generated.
        Otherwise, it should return None
    """
    dt = datetime.utcnow()

    file_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                              dt.month,
                                                              dt.day,
                                                              dt.hour,
                                                              dt.minute,
                                                              dt.second)

    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None

    if local("tar -cvzf {} web_static".format(file_name)).failed is True:
        return None

    return file_name
