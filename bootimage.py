#!/usr/bin/env python3

import sys
import subprocess

import common

if __name__ == '__main__':
    print(sys.argv)
    if not len(sys.argv) > 2:
        print("Invalid usage: " + sys.argv[0] + " <branchname> <devicename>")
        sys.exit(1)

    common.checkout_device(sys.argv[1])
#    common.sync()
    common.docker_pull()
    common.run_in_docker('/scripts/build_bootimage.sh ' + sys.argv[2] + " eng")
