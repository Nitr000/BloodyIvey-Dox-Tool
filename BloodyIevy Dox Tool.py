import os
import sys
import subprocess
import webbrowser
import time
from threading import Thread

def GTK():
    print("Creator:Nitro")
    print("Version 1.0")
    print("[10] Social Stalk")
    print("[20] Address Stalk")
    print("[30]Phone Stalk")
    print("\n")
    answer = raw_input("Enter:")

    if answer == "10":
       print("[1]Twitter Stalk")
       print("[2]Youtube Stalk")
       print("[3]Instagram Stalk")
       print("[4]Facebook Stalk")
       print("[5]Flickr Stalk")
       answer1 = raw_input("Enter:")

     
    if answer1 == "1":

       new=2

       tabUrl="https://twitter.com/search/";
       response = raw_input("Enter Twitter Alias:");
       print("Looking Through Database........")
       time.sleep(3)
      
        
       webbrowser.open(tabUrl+response,new=new);

    if answer1 == "2":

       new=2

       tabUrl="https://www.youtube.com/search/";
       response = raw_input("Enter Youtube Alias:");
       print("Looking Through Database..........")
       time.sleep(3)
       webbrowser.open(tabUrl+response,new=new);    
    
    if answer1 == "3":
       
       new=2
     
       tabUrl="https://www.instagram.com/explore/tags//?hl=en"
       response = raw_input("Enter Instagram #")
       print("Looking Through Databse..........")
       time.sleep(3)
       webbrowser.open(tabUrl+response,new=new);

    if answer1 == "4":
       
       new=2

       tabUrl="https://www.facebook.com/search/top/?q=" 
       response = raw_input("Enter Facebook Alias:")
       print("Looking Through Databse..........")
       time.sleep(3)
       webbrowser.open(tabUrl+response,new=new);
    
    if answer1 == "5":

      new=2

      tabUrl="https://www.flickr.com/search/?q="
      response = raw_input("Enter Flickr Alias:")
      print("Looking Through Databse..........")
      time.sleep(3)
      webbrowser.open(tabUrl+response,new=new);
    
       

GTK()
