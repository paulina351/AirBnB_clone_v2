#!/usr/bin/python3
<<<<<<< HEAD
# Fabfile to generates a .tgz archive from the contents of web_static.
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
=======
"""using fabric to generate archive from the contents"""
from fabric.api import local
from os.path import isdir
import datetime


def do_pack():
    """a Fabric script that generates a .tgz archive from the
    contents of the web_staticfolder of your AirBnB Clone repo,
    using the function do_pack.
    """
    try:
        day = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is false:
            local("mkdir versions")
        file_Func = "versions/web_static_{}.tgz".format(day)
        local("tar -czvf {} web_staic".format(fileFunc))
        return file_Func
    except FileNotFoundError:
        return None
>>>>>>> 5deed05b6952bc9554c76ee734006cbcef6542ee
