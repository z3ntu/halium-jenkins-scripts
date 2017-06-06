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

    workspace = os.getenv('WORKSPACE')
    if not workspace:
        print("This seems to not be run with Jenkins. The environment variable WORKSPACE is used by this script.")
        sys.exit(1)

    # Clean workspace directory
    for f in glob.glob(workspace + '/*'):
        os.remove(f)

    # Clean the out directory
    for f in glob.glob(common_ubuntu.out_location + '/' + sys.argv[1] + '-rootfs-*.tar.gz'):
        os.remove(f)

    # Build the rootfs
    common_ubuntu.run_in_docker('/scripts/build_rootfs.sh ' + sys.argv[1])

    # Check if file actually exists
    rootfs = glob.glob(common_ubuntu.out_location + '/' + sys.argv[1] + '-rootfs-*.tar.gz')
    if len(rootfs) != 1:
        print("Too many or no rootfs file(s): " + str(rootfs))
        sys.exit(1)

    # Move to workspace folder for jenkins archiving
    print(rootfs)
    filename = os.path.basename(rootfs[0])
    shutil.move(rootfs[0], workspace + "/" + filename)
    print("Moved " + rootfs[0] + " to " + workspace)

