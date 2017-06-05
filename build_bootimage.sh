#!/bin/bash

source build/envsetup.sh
breakfast "$1" "$2"
mka clobber
mka bootimage
if [ ! -f "$OUT/boot.img" ]; then
    echo "Making bootimage failed! \"$OUT/boot.img\" does not exist."
    exit 1
fi
echo "\"mka bootimage\" is finished."
