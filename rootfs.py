#!/usr/bin/env python3

import sys
import subprocess
import glob
import os
import shutil

import common_ubuntu

if __name__ == '__main__':
    print(sys.argv)
    if not len(sys.argv) > 1:
        print("Invalid usage: " + sys.argv[0] + " <branchname>")
        sys.exit(1)
    if not os.getenv('WORKSPACE'):
        print("This seems to not be run with Jenkins. The environment variable WORKSPACE is used by this script.")
        sys.exit(1)

    rootfs_old = glob.glob(common_ubuntu.out_location + '/' + sys.argv[1] + '-rootfs-*.tar.gz')
    if len(rootfs_old) > 0:
        print("Out directory already contains: " + str(rootfs_old))
        sys.exit(1)
    common_ubuntu.run_in_docker('/scripts/build_rootfs.sh ' + sys.argv[1])
    rootfs = glob.glob(common_ubuntu.out_location + '/' + sys.argv[1] + '-rootfs-*.tar.gz')
    if len(rootfs) != 1:
        print("Too many rootfs or no file(s): " + str(rootfs))
        sys.exit(1)

    print(rootfs)
    shutil.move(rootfs[0], os.getenv('WORKSPACE'))
    print("Moved " + rootfs[0] + " to " + os.getenv('WORKSPACE'))

