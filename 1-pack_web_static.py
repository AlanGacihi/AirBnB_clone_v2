#!/usr/bin/python3
""" Creates a tar with the webstatic """

import tarfile
import os
from datetime import datetime


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
