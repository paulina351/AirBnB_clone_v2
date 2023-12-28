#!/usr/bin/python3
<<<<<<< HEAD
# Fabfile to delete out-of-date archives.
import os
from fabric.api import *

env.hosts = ["104.196.168.90", "35.196.46.172"]


def do_clean(number=0):
    """Delete out-of-date archives.

    Args:
        number (int): The number of archives to keep.

    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
=======
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
>>>>>>> 5deed05b6952bc9554c76ee734006cbcef6542ee
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
<<<<<<< HEAD
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
=======
        arch = run("ls -tr").split()
        arch = [a for a in arch if "web_static_" in a]
        [arch.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in arch]
>>>>>>> 5deed05b6952bc9554c76ee734006cbcef6542ee
