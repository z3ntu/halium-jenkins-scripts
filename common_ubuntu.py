#!/usr/bin/env python3

import os
import subprocess

out_location = "/build/halium/out"
build_location = "/build/halium/rootfs"
scripts_location = os.path.dirname(os.path.realpath(__file__))
dockerimage = "ubuntu:artful"


def docker_pull():
    subprocess.check_call(['docker', 'pull', dockerimage])


def run_in_docker(command):
    # Flush here that the buffer is clear before the docker output comes.
    print("Running commands in docker image...", flush=True)
    subprocess.check_call(['docker', 'run', '--privileged', '--rm', '-v', scripts_location + ':/scripts', '-v',
                    build_location + ':/build', '-v', out_location + ':/out', dockerimage, '/bin/bash', '-c', command])
