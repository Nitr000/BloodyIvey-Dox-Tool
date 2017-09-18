import subprocess
from sys import platform
import webbrowser
subprocess.call("clear")
print("Creator:Nitro")
print("[1] Social Stalk Attack")
print("[2] Personal Informaion Attack")
print("[3] Attack!")
print("[4] Help")
print("\n")
choice = raw_input("Enter:")

#Check OS
if platform == "win32":
	subprocess.call("color a")


if choice == "1":
	execfile("social.py")

if choice == "4":
    execfile("help.py")

if choice == "2":
   execfile("Information.py")

if choice == "3":
   url = "https://paste.ee/"
   webbrowser.open_new(url)


 
