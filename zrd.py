#!/usr/bin/env python
from urllib2 import Request, urlopen, URLError, HTTPError
def Space(j):
        i = 0
        while i<=j:
                print " ",
                i+=1 
def banner():
	figlet -f small Chemod_zrd404
        
	print("\033[93m IndoCyber copyright(c)		   ")
	print("\033[96m http://generasicyberindo.blogspot.com	   ")
def miminEA():
        f = open("coretetek.txt","r");
        print("Masukin web nyah  \n(ex : pornhub.com atau www.pornhub.com ) ")
        link = raw_input("zrd@root : ")
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
