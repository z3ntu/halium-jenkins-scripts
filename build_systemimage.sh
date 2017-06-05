#!/bin/bash

source build/envsetup.sh
breakfast "$1" "$2"
mka clobber
mka systemimage
if [ ! -d "$OUT/system.img" ]; then
    echo "Making systemimage failed! \"$OUT/system.img\" does not exist."
    exit 1
fi
echo "\"mka systemimage\" is finished."
