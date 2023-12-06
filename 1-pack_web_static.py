#!/usr/bin/python3
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
