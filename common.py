#!/usr/bin/env python3

import subprocess
import os

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
    mounts = ['-v', android_location + ':/var/android', '-v', scripts_location + ':/scripts']
    s_command = ['docker', 'run', '--rm', '--net=host']
    s_command.extend(mounts)
    s_command.extend([dockerimage, '/bin/bash', '-c', command])
    subprocess.run(s_command, check=True)
