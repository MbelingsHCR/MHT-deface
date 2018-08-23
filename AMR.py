#!/usr/bin/env python
from urllib2 import Request, urlopen, URLError, HTTPError
def Space(j):
        i = 0
        while i<=j:
                print " ",
                i+=1 
def banner():
	print("\033[95m   _ _                        _                 _ _ _   __  _ _")
	print(" / __| |_  ___ _ __  ___  __| |      ____ _ __| | | | /  \| | |")
	print("\033[00m| (__| ' \/ -_) '  \/ _ \/ _` |     |_ / '_/ _` |_  _| () |_  _|")
	print(" \___|_||_\___|_|_|_\___/\__,_|__ __/__|_| \__,_| |_| \__/  |_|")
        print("                             |___|___| ")
	print("\033[93m IndoCyber copyright(c)		   ")
	print("\033[96m http://generasicyberindo.blogspot.com	   ")
def miminEA():
        f = open("coretetek.txt","r");
        print("Masukin web nyah  \n(contoh : website.com atau www.website.com ) ")
        link = raw_input("Chemod@zrd404 : ")
	print "\033[92m \n\nlink admin : \n"
        while True:
                sub_link = f.readline()
                if not sub_link:
                        break
                req_link = "http://"+link+"/"+sub_link
                req = Request(req_link)
                try:
                        response = urlopen(req)
                except HTTPError as e:
                        continue
                except URLError as e:
                        continue
                else:
                        print "OK => ",req_link

banner()
miminEA()
