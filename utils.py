import os
import subprocess

def checkRoot():
    if os.geteuid() != 0:
        print("Please run this script as root. (check the script if you don't really trust it)")
        exit()

def checkInternetConnection():
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
        os.system(f"sudo umount -f /dev/{partition}*")
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
    print("WARNING: This will delete all data on the SD card")
    # Ask for confirmation
    # confirm = input("Are you sure you want to continue? (y/n): ")
    # if confirm == "y":
    #     # use parted to partition the first 300MB of the SD card
        
    # full command:
    # ❯ sudo parted -a optimal /dev/sdX --script -- mklabel msdos mkpart primary fat32 0% 300MiB mkpart primary ext4 300MiB 100%
    table = f'mklabel msdos'
    boot_part = f'mkpart primary fat32 0% 300MiB'
    rootfs_part = f'mkpart primary ext4 300MiB 100%'
    subprocess.call(f"sudo parted -a optimal /dev/{partition} --script -- {table} {boot_part} {rootfs_part}", shell=True)

    # /dev/sdX1 to FAT
    print("Create the FAT partition...")
    os.system(f'sudo mkfs.vfat /dev/{partition}1 > /dev/null 2>&1')

    # /dev/sdX2 to ext4
    print("Create the ext4 partition...")
    os.system(f"sudo mkfs.ext4 /dev/{partition}2 > /dev/null 2>&1")

def mountSDCard(partition, temp_dir="./temp"):
    # Mount the partitions
    # os.system("sudo mount /dev/"+partition+"1 boot")
    # os.system("sudo mount /dev/" + partition + "2 root")
    
    print("Mounting partitions...")
    subprocess.call(f"sudo mount --mkdir /dev/{partition}1 {temp_dir}/boot", shell=True)
    subprocess.call(f"sudo mount --mkdir /dev/{partition}2 {temp_dir}/root", shell=True)

def downloadRootFS(root_fs_url, temp_dir="./temp"):
    print("Downloading the root filesystem...")
    subprocess.call(f'wget {root_fs_url} -P {temp_dir}', shell=True)

def extractRootFS(root_fs, temp_dir="./temp"):
    # Extract the root filesystem & sync
    print("Extracting & syncing the root filesystem...")
    print(f"sudo bsdtar -xpf {root_fs} - -C {temp_dir}/root")
    os.system(f"sudo bsdtar -xpf {root_fs} - -C {temp_dir}/root")
    os.system("sync")

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
    print(f"Creating temporary directory at {os.getcwd()}/temp")
    print(f'Formatting & partitioning /dev/{partition}...')
    formatSDCard(partition) # formatted + partitioned
    mountSDCard(partition)

    # Download root filesystem
    # Create temp directory
    downloadRootFS(root_fs_url)
    extractRootFS(root_fs)
    cleanup()
    
def cleanup():
    print("Cleaning up...")
    os.system("sudo rm -rf ./temp")
