#!/bin/bash

source build/envsetup.sh
breakfast "$1" "$2"
mka clobber
# Workaround for: /bin/bash: mkbootimg: command not found
mka mkbootimg
mka hybris-boot
if [ ! -f "$OUT/hybris-boot.img" ]; then
    echo "Making bootimage failed! \"$OUT/boot.img\" does not exist."
    exit 1
fi
echo "\"mka bootimage\" is finished."
