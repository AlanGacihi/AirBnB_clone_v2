#!/usr/bin/python3
""" Creates a tar with the webstatic """

import tarfile
import os
from datetime import datetime
from fabric.api import env
from fabric.operations import put, run
env.hosts = ["35.243.179.143", "35.237.105.68"]
env.user = "ubuntu"


def do_pack():
    """ Creates the tar file """
    newfile = "web_static_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".tgz"
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    with tarfile.open("versions/" + newfile, "w:gz") as f:
        f.add("web_static", arcname=os.path.basename("web_static"))
    if os.path.isfile("versions/" + newfile):
        return "versions/" + newfile
    else:
        return None


def do_deploy(archive_path):
    """ Makes the deployment """
    if not os.path.isfile(archive_path):
        return False
    try:
        filename = archive_path.split("/")[-1]
        put(archive_path, "/tmp/{}".format(filename))
        run("mkdir -p /data/web_static/releases/{}/".format(filename[:-4]))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(filename, filename[:-4]))
        run("rm /tmp/{}".format(filename))
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/\
releases/{}/".format(filename[:-4], filename[:-4]))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(filename[:-4]))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(filename[:-4]))
        return True
    except Exception:
        return False


def deploy():
    """ Makes the full deployment """
    packed = do_pack()
    if not packed:
        return False
    return do_deploy(packed)
