#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the contents of
# the web_static folder of your AirBnB Clone repo, using the
# function do_pack

import os.path
import time
from datetime import datetime
from fabric.api import local
from fabric.api import *
from fabric.operations import env, put, run

env.hosts = ["54.237.42.80", "54.221.185.211"]


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


def do_deploy(archive_path):
    '''Distrebute the file in the archive'''
    if os.path.exists(archive_path):
        archived_file = archive_path[9:]
        newest_version = "/data/web_static/releases/" + archived_file[:-4]
        archived_file = "/tmp/" + archived_file
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(newest_version))
        run("sudo tar -xzf {} -C {}/".format(archived_file, newest_version))
        run("sudo rm {}".format(archived_file))
        run("sudo mv {}/web_static/* {}".format(newest_version,
                                                newest_version))
        run("sudo rm -rf {}/web_static".format(newest_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newest_version))
        print("New version deployed!")
        return True

    return False


def deploy():
    ''' creates and distributes an archive '''
    path = do_pack()
    if path:
        return do_deploy(path)
    else:
        return False
