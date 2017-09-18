import os 
import sys
import subprocess
import webbrowser
import time

subprocess.call("clear")
print("[10] IP lookup")
print("[15] Indetity lookup")
print("[20] Resolver")
response =  raw_input("Enter:")

	
if response == "10":

	new=2

	tabUrl="http://ipinfodb.com/ip_locator.php/search/q="
	IP = raw_input("Enter IP:")
	time.sleep(1)
	print("Looking Through IP Databases......")
	time.sleep(2)
	print("Getting Geolocation.......")
	time.sleep(2)
	print("Success!")
    	webbrowser.open(tabUrl+response,new=new);



