<<<<<<< HEAD
bute an archive to a web server.
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ["104.196.168.90", "35.196.46.172"]


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True
=======
#!/usr/bin/python3
"""distributing an archive to our web server."""

from fabric.api import env, put, run
from os.path import exists
env.hosts = [' ']
env.user = 'ubuntu'
env.identity = '~/.ssh/school'
env.password = None


def do_deploy(archive_path):
    """Distributes an archive to a server."""
    if exists(archive_path) is False:
        return False
    try:
        file_func = archive_path.split("/")[-1]
        func = file_func.split(".")[0]
        path = "/data/web_static/release/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, func))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_func, path, func))
        run('rm /tmp/{}'.format(file_func))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, func))
        run('rm -rf {}{}/web_static'.format(path, func))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ / data/web_static/current'.format(path, func))
        run('chmod -R 755 /data/')
        print("New version deployed!")
        return True
    excepy FileNotFoundError:
        return False
>>>>>>> 5deed05b6952bc9554c76ee734006cbcef6542ee
