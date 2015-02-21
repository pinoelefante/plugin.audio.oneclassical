import urllib
import urllib2
import re
from BeautifulSoup import BeautifulSoup

#class ClassicalMusic:

class OneClassical:
	LIST_CATEGORY 	= "composer_type.php"
	LIST_OPERE		= "composer.php"
	OPERA 			= "title.php"
	
	def get_composer_list(self):	
		url = 'http://www.1classical.com/download_free_classical_music_MP3_browse_by_composer.php'
		response = urllib2.urlopen(url)
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
	
	