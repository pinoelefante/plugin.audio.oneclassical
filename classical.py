import urllib
import urllib2
import re
import xbmc
from BeautifulSoup import BeautifulSoup

#class ClassicalMusic:

class OneClassical:
	LIST_CATEGORY 	= "composer_type.php"
	LIST_OPERE		= "composer.php"
	OPERA 			= "title.php"
	
	def get_composer_list(self):	
		url = 'http://www.1classical.com/download_free_classical_music_MP3_browse_by_composer.php'
		response = urllib2.urlopen(url.replace(" ", "%20"))
		html = response.read()
		response.close()
		soup = BeautifulSoup(html);
		lista_autori = soup.table.findAll('a')
		list=[]
		for link in lista_autori:
			list.append([link.find(text=True), link.get("href")])
		return list
		
	def url_is_opera(self, url):
		return url.find(self.OPERA)>=0
	
	def url_is_category(self, url):
		return url.find(self.LIST_CATEGORY)>=0
	
	def url_is_list_opere(self, url):
		return url.find(self.LIST_OPERE)>=0
	
	def get_page_list(self, path):
		url = "http://www.1classical.com/"+path
		xbmc.log(url, level=xbmc.LOGNOTICE)
		response = urllib2.urlopen(url.replace(" ", "%20"))
		html = response.read()
		response.close()
		soup = BeautifulSoup(html);
		lista_autori = soup.table.findAll('a')
		list=[]
		for link in lista_autori:
			list.append([link.find(text=True), link.get("href")])
		return list
	
	def get_music_list(self, path):
		url = urllib.unquote_plus("http://www.1classical.com/"+path)
		print url
		response = urllib2.urlopen(url.replace(" ", "%20"))
		html = response.read()
		response.close()
		soup = BeautifulSoup(html);
		#print soup.prettify()
		
		links = soup.find("div", attrs={"id":"tempo"}).findAll("a")
		mp3=[]
		for link in links:
			mp3.append([link.find(text=True), link.get("href")])
			#print link.find(text=True) + " --- " + link.get("href")
		
		return mp3
		
		#lista_mp3=[]
		#if div.get("id") == "tempo":
		#	lista_mp3 = div.findAll('a')
			
		#list=[]
		#for link in lista_mp3:
		#	list.append([link.find(text=True), link.get("href")])
		#return list
	