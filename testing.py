import os
# os.system("sudo bsdtar -xpf ./ArchLinuxARM-rpi-armv7-latest.tar.gz - -C ./root")
# os.system("sudo fdisk -l | grep -i 'Disk /dev/'")
# print(list)

root_filesystem = "ArchLinuxARM-rpi-latest.tar.gz"
root_filesystem_url = "https://alaa.ad24.cz/repos/2022/02/06/os/" + root_filesystem

os.system("wget " + root_filesystem_url)