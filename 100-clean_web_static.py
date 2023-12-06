#!/usr/bin/python3
"""uses the function do_clean."""

import os
from fabric.api import *
env.hosts = [' ']
env.user = 'ubuntu'
env.identity = '~/.ssh/school'


def do_clean(number=0):
    """A fabric script that deletes out-of-date archives,
    using the function do_clean."""
    numer = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [arch.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        arch = run("ls -tr").split()
        arch = [a for a in arch if "web_static_" in a]
        [arch.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in arch]
