from splinter import Browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pprint import pprint
import re
import time
import os


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")

#chrome_options.add_experimental_option("disable-notifications", True)

browser = Browser('chrome', options=chrome_options)
# Visit URL
url = "http://www.facebook.com/login"
browser.visit(url)

while(True):
	op = input("facebook_pro_researcher# ")

	if(op == "save"):
		currentPage = re.search('https://www.facebook.com/(.+)', browser.url).group(1)
		browser.visit('https://www.facebook.com/' + currentPage + "/friends")
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
				friend = re.search('https://www.facebook.com/profile.php\?id=(.+?)&', a['href']).group(1)
			all+= friend + ";"
		
		try:
			os.mkdir(currentPage)
		except OSError as exc:
			print("Pasta já existe")
		
		arq = open(currentPage + "/friends.txt", 'w')
		arq.write(all)
		print("Lista de amigos salva.")
			
	elif(op == "compare")
    
