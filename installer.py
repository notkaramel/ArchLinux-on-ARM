import os
# Giving user options to install their desired OS
options = ["RasPi ARMv6", "RasPi ARMv7", "RasPi ARMv8"]
print("Welcome to the Raspberry Pi OS Installer")
print("Please select your Raspberry Pi OS:")
for i in range(len(options)):
    print("\t" + str(i) + ") " + options[i])
print("\t" + str(len(options)) + ") Exit")

print("Please select your Raspberry Pi OS: ", end="")
choice = input()
if choice == str(len(options)):
    print("Exiting...")
    exit()
else:
    print("Installing " + options[int(choice)])
    print("Please wait...")
    if int(choice) == 0:
        os.system("sudo cp -r rpi-armv6/RPi-ArchLinuxInstaller-ARMv6.py /home/pi/RPi-ArchLinuxInstaller-ARMv6.py")
        os.system("sudo chmod +x /home/pi/RPi-ArchLinuxInstaller-ARMv6.py")
        os.system("sudo /home/pi/RPi-ArchLinuxInstaller-ARMv6.py")
    elif int(choice) == 1:
        os.system("sudo cp -r rpi-armv7/RPi-ArchLinuxInstaller-ARMv7.py /home/pi/RPi-ArchLinuxInstaller-ARMv7.py")
        os.system("sudo chmod +x /home/pi/RPi-ArchLinuxInstaller-ARMv7.py")
        os.system("sudo /home/pi/RPi-ArchLinuxInstaller-ARMv7.py")
    elif int(choice) == 2:
        os.system("sudo cp -r rpi-armv8/RPi-ArchLinuxInstaller-ARMv8.py /home/pi/RPi-ArchLinuxInstaller-ARMv8.py")
        os.system("sudo chmod +x /home/pi/RPi-ArchLinuxInstaller-ARMv8.py")
        os.system("sudo /home/pi/RPi-ArchLinuxInstaller-ARMv8.py")
    else:
        print("Invalid choice.")
        exit()
    print("Done.")
    print("Exiting...")
    exit()


