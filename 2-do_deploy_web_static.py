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
