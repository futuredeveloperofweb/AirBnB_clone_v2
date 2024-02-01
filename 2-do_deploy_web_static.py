#!/usr/bin/python3
# Fabric script that distributes an archive to your web servers,
# using the function do_deploy
import os.path
from fabric.api import env, put, run

env.hosts = ["54.237.42.80", "54.221.185.211"]


def do_deploy(archive_path):
    """Distributes an archive to a web server."""
    if not os.path.isfile(archive_path):
        return False

    file_name = archive_path.split("/")[-1]
    name = file_name.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file_name)).failed:
        return False

    if run("rm -rf /data/web_static/releases/{}/".format(name)).failed:
        return False

    if run("mkdir -p /data/web_static/releases/{}/".format(name)).failed:
        return False

    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(file_name, name)).failed:
        return False

    if run("rm /tmp/{}".format(file_name)).failed:
        return False

    if run("mv / data/web_static/releases/{}/web_static/*
            / data/web_static/releases/{} /".format(name, name)).failed:
        return False

    if run("rm -rf /data/web_static/releases/{}/web_static"
            .format(name)).failed:
        return False

    if run("rm -rf /data/web_static/current").failed:
        return False

    if run("ln - s / data/web_static/releases/{} /
            /data/web_static/current".format(name)).failed:
        return False

    return True
