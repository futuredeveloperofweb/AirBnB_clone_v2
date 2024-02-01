#!/usr/bin/python3
# A Fabric script that generates a .tgz archive from the contents
# of the web_static folder of your AirBnB Clone repo, using the
# function do_pack
from datetime import datetime
from fabric.api import local
from fabric.decorators import runs_once
import os.path


def do_pack():
    '''
    create a tar to collect all the files in web_static folder in one
    archive file

    Returns:
        archive path if the archive has been correctly generated,
        otherwise; it should return None
    '''

    file_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                              dt.month,
                                                              dt.day,
                                                              dt.hour,
                                                              dt.minute,
                                                              dt.second)

    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None

    if local("tar -cvzf {} web_static".format(file_n)).failed is True:
        return None
    return file_n
