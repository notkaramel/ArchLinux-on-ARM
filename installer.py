#!/usr/bin/python3
import utils, os

# Checking if the user is root
utils.checkRoot()

# Checking if the user is connected to the internet
utils.checkInternetConnection()

try:
    choice = utils.menu()
    utils.install(choice)
    print("place holder")
except KeyboardInterrupt:
    print("\nCleaning up...")
    os.system("sudo rm -rf ./temp")
    exit()
