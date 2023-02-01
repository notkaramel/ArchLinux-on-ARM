# ArchLinux installer for Raspberry Pi
![MIT License](https://img.shields.io/github/license/notkaramel/ArchLinux-ARM-Installer)
### Version: 1.1.1
### Description:
This is a minimal installer script to install ArchLinux ARM (v7) onto a Raspberry Pi 400. It should also work on all Raspberry Pi models that supports ARMv7 (e.g., Raspberry Pi 4)

### Requirements:
- An SD Card (I used a 32GB SD Card when I tested this)
- python3, bash, bsdtar
- Host PC's operating system must be Linux (e.g., Arch Linux)
- NOTE: I don't really know if this would work on a MacOS or Windows PC. If you have any feedback/ have done any testings, please let me know.

### Usage:
```bash
git clone https://github.com/notkaramel/ArchLinux-ARM-Installer.git
cd ArchLinux-ARM-Installer
python3 installer.py
```
> **NOTE**: Please read through the scripts before running them. You may adjust the code to suit your personal machine. 

- After the program finishes, make sure that there is no errors in the terminal.
- Plug in the SD Card into your Raspberry Pi of choice. If everything works, you should see a welcome message. (Congrats!!)
- Login as the root user by typing directly into the empty terminal **```root```** user and **```root```** as the password.
```bash
root
Password: # root
```
- Please follow [ArchLinux ARM RPi4 Installation Guide](https://archlinuxarm.org/platforms/armv8/broadcom/raspberry-pi-4) to finish the installation on your Raspberry Pi. Basically it's just:
```bash
pacman-key --init
pacman-key --populate archlinuxarm
```
### Contribution:
- If you have any suggestions/feedback/improvements, all contributions are very welcome.
- How to? You can follow this [article](https://gist.github.com/MarcDiethelm/7303312). TL;DR: fork, clone, edit, push, and submit a pull request.

### Notes:
- I made this to reduce the time it takes to install ArchLinux (ARMv7) on my Raspberry Pi 400.
- It should also work for all models of Raspberry Pi 4, hopefully.
- A similar script for ARMv8/aarch64 will be updated ASAP!
- I designed this script based on the [ArchLinux ARM RPi4 Installation Guide](https://archlinuxarm.org/platforms/armv8/broadcom/raspberry-pi-4). Credit goes to the authors!
