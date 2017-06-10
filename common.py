#!/usr/bin/env python3

import glob
import os
import shutil
import subprocess

out_location = "/build/halium/out"
android_location = "/build/halium/android"
scripts_location = os.path.dirname(os.path.realpath(__file__))
dockerimage = "z3ntu/fairphone2-build-env-with-vim"


def checkout_device(device):
    print("Fetching...")
    subprocess.run(['git', '-C', android_location + '/.repo/local_manifests', 'fetch'], check=True)
    print("Checking out...")
    subprocess.run(['git', '-C', android_location + '/.repo/local_manifests', 'checkout', device], check=True)


def sync():
    print("Syncing...")
    subprocess.run(['repo', 'sync', '-j4', '-c'], cwd=android_location, check=True)


def docker_pull():
    subprocess.run(['docker', 'pull', dockerimage], check=True)


def run_in_docker(command):
    # Flush here that the buffer is clear before the docker output comes.
    print("Running commands in docker image...", flush=True)
    mounts = ['-v', android_location + ':/var/android', '-v', scripts_location + ':/scripts', '-v',
              out_location + ':/out']
    s_command = ['docker', 'run', '--rm', '--net=host']
    s_command.extend(mounts)
    s_command.extend([dockerimage, '/bin/bash', '-c', command])
    subprocess.run(s_command, check=True)


def get_workspace_loc():
    workspace = os.getenv('WORKSPACE')
    if not workspace:
        print("This seems to not be run with Jenkins. The environment variable WORKSPACE is used by this script.")
        sys.exit(1)
    return workspace


def clean_directory(directory):
    # Clean workspace directory
    for f in glob.glob(directory + '/*'):
        os.remove(f)


def check_that_one_file_exists(filepath):
    # Check if file actually exists
    rootfs = glob.glob(filename)
    if len(rootfs) != 1:
        print("Too many or no file(s): " + str(rootfs))
        sys.exit(1)
    return rootfs[0]


def move_to_workspace(filepath, workspace):
    shutil.move(filepath, workspace + "/" + os.path.basename(filepath))
    print("Moved " + filepath + " to " + workspace)
