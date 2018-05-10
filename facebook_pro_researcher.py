from splinter import Browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pprint import pprint
import re
import time
import os

browser = 0

def openTab(url):
	browser.execute_script("window.open('" + url + "','_blank');")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")



global_list = []

while(True):
	command = input("facebook_pro_researcher# ")
	command += " "
	
	c = re.search("(.+?) (.*)", command).groups()
	op = c[0]
	args = c[1].split(" ")[0:-1]

	if(op == "save"):
		currentPage = re.search('https://www.facebook.com/(.+)[&/]', browser.url).group(1)

		scrollHeight = browser.evaluate_script("document.body.scrollHeight")
		scrollTop = browser.evaluate_script("document.documentElement.scrollTop")
		innerHeight = browser.evaluate_script("window.innerHeight")
		
		while(scrollTop + innerHeight < scrollHeight):
			browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
			time.sleep(2)
			print("scrolling")
			scrollHeight = browser.evaluate_script("document.body.scrollHeight")
			scrollTop = browser.evaluate_script("document.documentElement.scrollTop")
			innerHeight = browser.evaluate_script("window.innerHeight")
		
		friends = browser.find_by_css("._698")
		print("exit")
		all = ""
		for f in friends:
			a = f.find_by_tag("a")
			friend = re.search('https://www.facebook.com/(.+?)\?', a['href']).group(1)
			if(friend == "profile.php"):
				friend = re.search('https://www.facebook.com/(profile.php\?id=(.+?))&', a['href']).group(1)
			all+= friend + ";"
		
		try:
			os.mkdir(currentPage)
		except OSError as exc:
			print("Pasta já existe")
		
		arq = open(currentPage + "/friends.txt", 'w')
		arq.write(all)
		print("Lista de amigos salva.")
			
	elif(op == "intersec"):
		intersec = open(args[0] + "/friends.txt", 'r').read().split(";")[0:-1]

		for i in range(1, len(args)):
			intersec = set(open(args[i] + "/friends.txt", 'r').read().split(";")).intersection(intersec)
		
		intersec = list(intersec)

		for i in range(0, len(intersec)):
			print(str(i) + " - " + intersec[i])
		global_list = intersec
	elif(op == "browser"):
		browser = Browser('chrome', options=chrome_options)
		url = "http://www.facebook.com/login"
		browser.visit(url)
	elif(op == "open"):
		if(args[0] == "all"):
			for i in global_list:
				url = "http://www.facebook.com/" + i
				openTab(url)
		else:
			for arg in args:
				url = "http://www.facebook.com/" + global_list[int(arg)]
				openTab(url)

		
    
