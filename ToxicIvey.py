import subprocess
from sys import platform
print("Creator:Nitro")
print("[1] Social Stalk")
print("[2] Personal Informaion")
print("[3] Help")
print("\n")
choice = input("")

#Check OS
if platform == "win32":
	subprocess.call("color a")


if choice == "1":
	execfile("social.py")

if choice == "3":
    execfile("help.py")

if choice == "2":
   execfile("Information.py")


 
