import os

# Variables:
root_filesystem = "ArchLinuxARM-2022.03-rpi-aarch64-rootfs.tar.gz"
# root_filesystem_url = "http://os.archlinuxarm.org/os/" + root_filesystem

root_filesystem_url = "https://alaa.ad24.cz/repos/2022/07/23/os/rpi/" + root_filesystem

# Select SD card partition name via input
print("Available partitions:")
os.system("sudo fdisk -l | grep -i 'Disk /dev/'")

# Select SD card partition name
print("Select SD card partition name (e.g.: sdb): ", end="")
partition = input()

# Make sure the partition is not mounted
print("Checking if the partition is mounted...")
if os.path.exists("/dev/" + partition):
    print("Partition is mounted, unmounting...")
    os.system("sudo umount /dev/" + partition)

# Ask if the use have already formatted the partition
formatted = input("Have you already formatted the partition? (y/n): ")
# if no, enter formatting step
if formatted == "n":
    print("Entering fdisk partition mode, good luck!")
    print("""
        o -> clear out any partitions on the drive.
        p -> list partitions. There should be no partitions left.
        n, p, ENTER, ENTER, +300M -> create first partition.
        t, c -> set type to W95 FAT32 (LBA).
        n, p, ENTER, ENTER, ENTER, -> create second partition (/root/).
        w -> write the partition table and exit.""")
    os.system("sudo fdisk /dev/" + partition)

else:
    print("Skipping fdisk partition mode, let's go!")

# /dev/sdX1 to FAT
print("Create the FAT partition...")
os.system("sudo mkfs.vfat /dev/" + partition + "1")

# /dev/sdX2 to ext4
print("Create the ext4 partition...")
os.system("sudo mkfs.ext4 /dev/" + partition + "2")

# After [skipping] partition
if(os.path.exists("boot")):
    print("boot directory already exists.")
else:
    print("Creating boot directory...")
    os.system("mkdir boot")

if(os.path.exists("root")):
    print("root directory already exists.")
else:
    print("Creating root directory...")
    os.system("mkdir root")

# Mount the partitions
print("Mounting partitions...")
os.system("sudo mount /dev/"+partition+"1 boot")
os.system("sudo mount /dev/" + partition + "2 root")

# Check if the root filesystem is installed
if os.path.exists(root_filesystem):
    print("Root filesystem is already installed.")
else:
    # Download and extract the root filesystem
    print("Downloading the root filesystem...")
    os.system("wget " + root_filesystem_url)

# Extract the root filesystem & sync
print("Extracting & syncing the root filesystem...")
print("sudo bsdtar -xpf " + root_filesystem + " - -C root")
os.system("sudo bsdtar -xpf " + root_filesystem + " - -C root")
os.system("sync")

# Move boot files to the first partition
# NOTE: Since mv has issues with the installation, we will use cp instead, then rm the original files
print("Moving boot files to the first partition...")
os.system("sudo cp -r root/boot/* boot/")
os.system("sudo rm -rf root/boot")

# aarch64 before unmounting the partitions instruction
os.system("sudo sed -i 's/mmcblk0/mmcblk1/g' root/etc/fstab")

# Unmount partitions
print("Unmounting partitions...")
os.system("sudo umount boot root")
print("Done!\n")
