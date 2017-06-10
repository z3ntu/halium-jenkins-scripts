#!/usr/bin/env python3

import subprocess
import os

android_location = "/build/halium/android"
scripts_location = os.path.dirname(os.path.realpath(__file__))
dockerimage = "z3ntu/fairphone2-build-env-with-vim"

def checkout_device(device):
    print("Fetching...")
    subprocess.check_call(['git', '-C', android_location + '/.repo/local_manifests', 'fetch'])
    print("Checking out...")
    subprocess.check_call(['git', '-C', android_location + '/.repo/local_manifests', 'checkout', device])

def sync():
    print("Syncing...")
    subprocess.check_call(['repo', 'sync', '-j4', '-c'], cwd=android_location)

def docker_pull():
    subprocess.check_call(['docker', 'pull', dockerimage])


def run_in_docker(command):
    # Flush here that the buffer is clear before the docker output comes.
    print("Running commands in docker image...", flush=True)
    mounts = ['-v', android_location + ':/var/android', '-v', scripts_location + ':/scripts']
    s_command = ['docker', 'run', '--rm', '--net=host']
    s_command.extend(mounts)
    s_command.extend([dockerimage, '/bin/bash', '-c', command])
    subprocess.check_call(s_command)

