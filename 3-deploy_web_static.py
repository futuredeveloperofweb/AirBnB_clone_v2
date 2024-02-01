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
    if (os.path.isfile(archive_path) is False):
        return False
    try:
        file = archive_path.split("/")[-1]
        folder = ("/data/web_static/releases/" + file.split(".")[0])
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(folder))
        run("tar -xzf /tmp/{} -C {}".format(file, folder))
        run("rm /tmp/{}".format(file))
        run("mv {}/web_static/* {}/".format(folder, folder))
        run("rm -rf {}/web_static".format(folder))
        run('rm -rf /data/web_static/current')
        run("ln -s {} /data/web_static/current".format(folder))
        print("Deployment done")
        return True
    except:
        return False


def deploy():
    ''' creates and distributes an archive '''
    path = do_pack()
    if path:
        return do_deploy(path)
    else:
        return False
