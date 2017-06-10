#!/usr/bin/env python3

import os
import sys

import common
import common_ubuntu

if __name__ == '__main__':
    print(sys.argv)
    if not len(sys.argv) > 1:
        print("Invalid usage: " + sys.argv[0] + " <branchname>")
        sys.exit(1)

    # Get workspace location
    workspace = common.get_workspace_loc()

    # Clean workspace directory
    common.clean_directory(workspace)

    # Clean the out directory
    common.clean_directory(common.out_location)

    # Build the rootfs
    common_ubuntu.run_in_docker('/scripts/build_rootfs.sh ' + sys.argv[1])

    # Check if file actually exists
    rootfs = common.check_one_file_exists(common.out_location + '/' + sys.argv[1] + '-rootfs-*.tar.gz'

    # Move to workspace folder for jenkins archiving
    common.move_to_workspace(rootfs, workspace)
