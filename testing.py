import os
# os.system("sudo bsdtar -xpf ./ArchLinuxARM-rpi-armv7-latest.tar.gz - -C ./root")
os.system("sudo fdisk -l | grep -i 'Disk /dev/'")
print(list)
