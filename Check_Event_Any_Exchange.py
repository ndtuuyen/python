from bs4 import BeautifulSoup
import urllib.request
from datetime import datetime
now = datetime.now().time()
def probit():

	f = open("link.txt", "r")
	s = open("exchange.txt", "r")
	
	#print(links)
	for url in f:
		#print(url)
		#break
		ex = s.readline()
		page = urllib.request.urlopen(url)
		soup = BeautifulSoup(page, 'html.parser')
		new_feed = soup.find('ul', class_='article-list').find('a')
		title = new_feed.get('title')
		x = new_feed.get('href')
		fo = open("data.txt", "r+")
		line = fo.read()
		if ( x in line ):
			print (ex ,": None")
		else:
			print (ex,x)
			file1 = open("data.txt","a")
			file1.write(x)
			file1.write("\n")
probit()