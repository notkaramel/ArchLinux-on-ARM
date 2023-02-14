# ArchLinux installer for Raspberry Pi
![MIT License](https://img.shields.io/github/license/notkaramel/ArchLinux-ARM-Installer)
### Version: 1.1.1 | Last updated: 2023-Feb-02

### Description:
A minimal CLI script to install ArchLinuxARM to an ARM device. Currently compatible and tested successfully on Raspberry Pi 3B+ and 400 (meaning it should supports ARMv7 compatible Raspberry Pi devices).

### Available options:
- ARMv6 on RPi (Zero, Zero W) (Cortex A7)
- ARMv7 on RPi (3, 3B+, 4, 400) (Cortex A53, A72)
- ARMv8 on RPi (4, 400) (Cortex A72)
- See more: [Compability](Compatibility.md)

### Requirements:
- An SD Card
  - 300 MiB will be used for the ```boot``` partition
  - The rest will be used for the ```root``` partition
- Packages use (need implementation to enforce dependencies)
  - On system: ```python3```, ```bash```, ```bsdtar```, ```wget```
  - Python packages: ```os```, ```subprocess```, ```time```, ```sys``` (```threading``` will be required for future feature)
- Host PC's operating system must be Linux (e.g., Arch Linux, Ubuntu, etc.)

### Usage:
```bash
git clone https://github.com/notkaramel/ArchLinux-ARM-Installer.git
cd ArchLinux-ARM-Installer
```

You may run the installer directly, or ```chmod +x``` the script and run it.
```bash
chmod +x installer.py
./installer.py
```
Alternatively, the more intuitive way is to run the script with python3:
```bash
python3 installer.py
```

> **NOTE**: Please read through the scripts before running them.

- After the program finishes, make sure that there is no errors in the terminal.
- Plug in the SD Card into your Raspberry Pi of choice. If everything works, you should see a welcome message. (Congrats!!)
- Login as the root user by typing directly into the empty terminal **```root```** user and **```root```** as the password.
```bash
root
Password: # root
```
- Please follow [ArchLinuxARM RPi4 Installation Guide](https://archlinuxarm.org/platforms/armv8/broadcom/raspberry-pi-4) to finish the installation on your Raspberry Pi. Basically it's just:
```bash
pacman-key --init
pacman-key --populate archlinuxarm
```

### Tasks and TODOs (public contribution needed!)
- [ ] Add support for ARMv8/aarch64
- [ ] Animation/Progress bar for the installation (and ```bsdtar```, ```cp```) process
- [ ] More testing and looking for edge cases
- [ ] Add support for other ARM devices (Chromebook, Zedboard, etc.)
- [ ] Add versions for Windows and MacOS

### Contribution guidelines:
- If you have any suggestions/feedback/improvements, all contributions are very welcome.
- How to? You can follow this [article](https://gist.github.com/MarcDiethelm/7303312). TL;DR: fork, clone, edit, push, and submit a pull request.

### Personal notes:
- I made this to **significantly** reduce the time it takes to install ArchLinux on my Raspberry Pi 400.
- I designed this script based on the [ArchLinux ARM RPi4 Installation Guide](https://archlinuxarm.org/platforms/armv8/broadcom/raspberry-pi-4). Credit goes to the authors!
- Feel free to contribute to the project! 
