from bs4 import BeautifulSoup
import urllib.request
from datetime import datetime
now = datetime.now().time()
def probit():
	url =  'https://support.probit.com/hc/en-us/sections/360003404611-Events'
	page = urllib.request.urlopen(url)
	soup = BeautifulSoup(page, 'html.parser')

	new_feed = soup.find('ul', class_='article-list').find('a')
	title = new_feed.get('title')
	x = new_feed.get('href')
	fo = open("data.txt", "r+")
	line = fo.read()
	if ( title in line ):
		print ("Probit : None")
	else:
		print ("Probit: ",title)
		file1 = open("data.txt","a")
		file1.write(title)
		file1.write("\n")
probit()

def bw():
	url =  'https://bwexchange.zendesk.com/hc/en-us/sections/360003872191-Important-Announcements'
	page = urllib.request.urlopen(url)
	soup = BeautifulSoup(page, 'html.parser')

	new_feed = soup.find('ul', class_='article-list').find('a')
	title = new_feed.get('title')
	x = new_feed.get('href')
	fo = open("data.txt", "r+")
	line = fo.read()
	if ( x in line ):
		print ("Bw : None")
	else:
		print ("Bw: ",x)
		file1 = open("data.txt","a")
		file1.write(x)
		file1.write("\n")

bw()
#
def bitmart():
	url =  'https://bitmart.zendesk.com/hc/en-us/sections/115000951153-Latest-News'
	page = urllib.request.urlopen(url)
	soup = BeautifulSoup(page, 'html.parser')

	new_feed = soup.find('ul', class_='article-list').find('a')
	title = new_feed.get('title')
	x = new_feed.get('href')
	fo = open("data.txt", "r+")
	line = fo.read()
	if ( x in line ):
		print ("Bitmart : None")
	else:
		print ("Bitmart: ",x)
		file1 = open("data.txt","a")
		file1.write(x)
		file1.write("\n")

bitmart()
def lbank():
	url =  'https://lbankinfo.zendesk.com/hc/en-gb/categories/900000043146-Announcements'
	page = urllib.request.urlopen(url)
	soup = BeautifulSoup(page, 'html.parser')

	new_feed = soup.find('ul', class_='article-list').find('a')
	title = new_feed.get('title')
	x = new_feed.get('href')
	fo = open("data.txt", "r+")
	line = fo.read()
	if ( x in line ):
		print ("Lbank : None")
	else:
		print ("Lbank: ",x)
		file1 = open("data.txt","a")
		file1.write(x)
		file1.write("\n")
lbank()
def hotbit():
	url =  'https://hotbit.zendesk.com/hc/en-us/sections/115001049054-News-and-Announcements'
	page = urllib.request.urlopen(url)
	soup = BeautifulSoup(page, 'html.parser')

	new_feed = soup.find('ul', class_='article-list').find('a')
	title = new_feed.get('title')
	x = new_feed.get('href')
	fo = open("data.txt", "r+")
	line = fo.read()
	if ( x in line ):
		print ("hotbit : None")
	else:
		print ("hotbit: ",x)
		file1 = open("data.txt","a")
		file1.write(x)
		file1.write("\n")
hotbit()

def bigone():
	url =  'https://bigone.zendesk.com/hc/en-us/categories/900000022243-Announcement'
	page = urllib.request.urlopen(url)
	soup = BeautifulSoup(page, 'html.parser')

	new_feed = soup.find('ul', class_='article-list').find('a')
	title = new_feed.get('title')
	x = new_feed.get('href')
	fo = open("data.txt", "r+")
	line = fo.read()
	if ( x in line ):
		print ("bigone : None")
	else:
		print ("bigone: ",x)
		file1 = open("data.txt","a")
		file1.write(x)
		file1.write("\n")
bigone()

