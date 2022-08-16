#!/usr/bin/python3

import os

# Giving user options to install their desired OS
options = ["ArchLinux ARMv6 on RPi", "ArchLinux ARMv7 on RPi", "ArchLinux ARMv8 on RPi"]

print("Welcome to the Raspberry Pi OS Installer")
print("List of available options:")
for i in range(len(options)):
    print("\t[" + str(i) + "] " + options[i])
print("\t[" + str(len(options)) + "] Exit")

print("Please select your Raspberry Pi OS: ", end="")
choice = input()

if choice == str(len(options)):
    print("Exiting...")
    exit()
else:
    print("Installing " + options[int(choice)])
    if int(choice) == 0:
        os.system("chmod +x ./rpi-armv6/RPi-ArchLinuxInstaller-ARMv6.py")
        os.system("sudo ./rpi-armv6/RPi-ArchLinuxInstaller-ARMv6.py")
    elif int(choice) == 1:
        os.system("chmod +x ./rpi-armv7/RPi-ArchLinuxInstaller-ARMv7.py")
        os.system("sudo ./rpi-armv7/RPi-ArchLinuxInstaller-ARMv7.py")
    elif int(choice) == 2:
        os.system("chmod +x ./rpi-armv8/RPi-ArchLinuxInstaller-ARMv8.py")
        os.system("sudo ./rpi-armv8/RPi-ArchLinuxInstaller-ARMv8.py")
    else:
        print("Invalid choice.")
        exit()
    print("Done!")
    exit()


