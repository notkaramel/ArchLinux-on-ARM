import os
import subprocess

def checkRoot():
    if os.geteuid() != 0:
        print("Please run this script as root. (check the script if you don't really trust it)")
        exit()

def checkInternetConnection():
    print("Checking internet connection...", end="")
    p = subprocess.call("ping -c 3 -q google.com >&/dev/null", shell=True)
    if p == 0:
        print("OK")
    else:
        print("Failed")
        print("Please check your internet connection and try again.")
        exit()

def menu() -> int:
    # Giving user options to install their desired OS
    options = ["[RPi] ArchLinux ARMv6", "[RPi] ArchLinux ARMv7", "[RPi] ArchLinux ARMv8"]

    print("Welcome to the Raspberry Pi OS Installer")
    print("List of available options:")
    for i in range(len(options)):
        print(f'\t[{i}] {options[i]}')
    print(f'\tCtrl + C to Exit')


    print("Please select your Raspberry Pi OS: ", end="")
    choice = int(input())
    if choice > len(options):
        print("Invalid choice.")
        exit()
    else:
        return choice

def findSDCard() -> str:
    # Select SD card partition name via input
    print("Available partitions:")
    # os.system("sudo fdisk -l | grep -i 'Disk /dev/'")
    os.system("sudo lsblk -o NAME,SIZE,MODEL,TRAN -d")
    # Make sure the partition is not mounted
    partition = input("Select SD card partition name (e.g.: sdb): ")

    if os.path.exists(f"/dev/{partition}"):
        print("Found partition")
        print("Partition is mounted, unmounting...")
        os.system(f"sudo -f umount /dev/{partition}")
        return partition
    else:
        print("Partition not found, try again or Ctrl + C to exit.")
        try: 
            findSDCard()
        except KeyboardInterrupt:
            exit()

    # Select SD card partition name
    

def formatSDCard(partition):
    print("Using parted to partition your SD card")
    # TODO

    # /dev/sdX1 to FAT
    print("Create the FAT partition...")
    os.system("sudo mkfs.vfat /dev/" + partition + "1")

    # /dev/sdX2 to ext4
    print("Create the ext4 partition...")
    os.system("sudo mkfs.ext4 /dev/" + partition + "2")

def partitionSDCard(partition):
    # TODO
    pass

def mountSDCard(partition):
    # Mount the partitions
    # os.system("sudo mount /dev/"+partition+"1 boot")
    # os.system("sudo mount /dev/" + partition + "2 root")
    
    print("Mounting partitions...")
    subprocess.call(f"sudo mount --mkdir /dev/{partition}1 ./temp/boot")
    subprocess.call(f"sudo mount --mkdir /dev/{partition}2 ./temp/root")

def downloadRootFS(root_fs_url):
    print("Downloading the root filesystem...")
    subprocess.call(f'wget {root_fs_url} ./temp')


def install(choice): # Perform clean installation
    # Hardcoded options, sorry :(
    fs_list = ["", "armv7-", "aarch64-"]
    root_fs = f'ArchLinuxARM-rpi-{fs_list[choice]}latest.tar.gz'
    root_fs_url = ""
    if choice == 0:
        # FROM THIS THREAD: https://forums.raspberrypi.com/viewtopic.php?t=326235
        root_fs_url += f"https://alaa.ad24.cz/repos/2022/02/06/os/{root_fs}"
    else:
        root_fs_url += f'http://os.archlinuxarm.org/os/{root_fs}'
    
    # Format SD card
    partition=findSDCard()
    formatSDCard(partition)
    partitionSDCard(partition)
    mountSDCard(partition)



    
    # After [skipping] partition
    
    exit()