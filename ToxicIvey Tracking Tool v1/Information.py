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
        
        #IP lookup
     	lib = raw_input("Enter IP:")
    	url = "http://whatismyipaddress.com/ip/" +(str(lib))+ "&_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
    	webbrowser.open_new(url)

if response == "15":
	lib = raw_input("Full Name:")	
    	url = "http://www.whitepages.com/name/" +(str(lib))
    	webbrowser.open_new(url)

if response == "20":
	lib = raw_input("Enter Tracking Url:")
    	url = "https://grabify.link/track/" +(str(lib))+ ""+(str(lib))+"&_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
    	webbrowser.open_new(url)
