#!/bin/bash

set -e

apt-get update && apt-get install -y git live-build qemu-user-static nano
update-binfmts --enable

cd /build
if [ ! -d "rootfs-builder" ]; then
    git clone https://github.com/bhush9/rootfs-builder -b $1
    cd rootfs-builder
else
    cd rootfs-builder
    currentbranch=$(git rev-parse --symbolic-full-name --abbrev-ref HEAD)
    if [ -f ".lock" ]; then
        git clean -fdx
    fi
    git checkout $1
fi
./build.sh
if [ ! -f "halium.rootfs.tar.gz" ]; then
    echo "\"halium.rootfs.tar.gz\" does not exist."
    exit 1
fi
echo "rootfs is finished."
cp halium.rootfs.tar.gz /out/$1-rootfs-$(date --iso).tar.gz
