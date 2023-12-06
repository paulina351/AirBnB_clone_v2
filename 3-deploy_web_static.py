#!/usr/bin/python3
"""distrubutes to the web server."""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = [' ']
env.user = 'ubuntu'
env.identity = '~/.ssh/school'


def do_pack():
    """that creates and distributes an archive to your web
    servers, using the function deploy
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_P = "versions/web_static_{}.tgz"format(date)
        local("tar -cvzf {} web_static".format(file_P))
        return file_P
    except FileNotFoundError:
        return None


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_func = archive_path.split("/")[-1]
        no_exit = file_path.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_exit))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_func, path, no_exit))
        run('rm /tmp/{}'.format(file_func))
        run('mv {0}{1}/web_static/* {)}{1}/'.format(path, no_exit))
        run('rm -rf {}{}/web_static'.format, no_exit))
        run('rm -rf /data/web_static.current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_exit))
        return True
    except FileNotFoundError:
        return False


def deploy():
    """distributes an archive to the web server."""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
