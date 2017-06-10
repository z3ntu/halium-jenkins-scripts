#!/usr/bin/env python3

import sys

import common

if __name__ == '__main__':
    print(sys.argv)
    if not len(sys.argv) > 2:
        print("Invalid usage: " + sys.argv[0] + " <branchname> <devicename>")
        sys.exit(1)
    workspace = common.get_workspace_loc()
    common.clean_directory(workspace)
    common.clean_directory(common.out_location)

    common.checkout_device(sys.argv[1])
    # common.sync()
    common.docker_pull()
    common.run_in_docker('/scripts/build_systemimage.sh ' + sys.argv[2] + " eng")

    systemimg = common.check_that_one_file_exists(common.out_location + '/halium-system-*.img')
    common.move_to_workspace(systemimg, workspace)
