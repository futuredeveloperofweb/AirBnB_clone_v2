#!/usr/bin/python3
# A Fabric script that generates a .tgz archive from the contents
# of the web_static folder of your AirBnB Clone repo, using the
# function do_pack

import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    '''
    create a tar to collect all the files in web_static folder in one
    archive file

    Returns:
        archive path if the archive has been correctly generated,
        otherwise; it should return None
    '''
    d = datetime.utcnow()

    f_n = 'versions/web_static_{}{}{}{}{}{}.tgz'
    .format(d.year, d.month, d.day, d.hour, d.minute, d.second)

    if os.path.isdir('versions') is False:
        if local('mkdir -p versions').failed is True:
            return None

    if local('tar -cvzf {} web_static'.format(f_n)).failed is True:
        return None
    return f_n
