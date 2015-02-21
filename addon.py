import os
import sys
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
import urllib
import urlparse
from classical import OneClassical

__plugin__ = "plugin.audio.oneclassical"
__author__ = "pinoelefante"

Addon = xbmcaddon.Addon(id=__plugin__)

handle = int(sys.argv[1])

provider = OneClassical()

def parameters_string_to_dict(parameters):
    paramDict = dict(urlparse.parse_qsl(parameters[1:]))
    return paramDict

def parameters (p):
    urlenc = urllib.quote_plus(p)
    return "plugin://"+__plugin__+"/?param="+urlenc

def addDir (s,p):
    item = xbmcgui.ListItem(s)
    return xbmcplugin.addDirectoryItem(handle=handle, url=parameters(p), listitem=item, isFolder=True)

def addItem (s,p):
    item = xbmcgui.ListItem(label=s)
    return xbmcplugin.addDirectoryItem(handle=handle, url=parameters(p), listitem=item, isFolder=False)

def list_composers():
    list = provider.get_composer_list()
    i = 0
    while i<len(list):
        addDir(list[i][0], list[i][1])
        i = i + 1
    xbmcplugin.endOfDirectory(handle=handle, succeeded=True)

def load_page(url):
    if provider.url_is_opera(url):
        print "pagina con mp3"
        list = provider.get_music_list(path=url)
        i = 0
        while i<len(list):
            addItem(list[i][0], list[i][1])
            i = i + 1
        xbmcplugin.endOfDirectory(handle=handle, succeeded=True)
    else:
        list = provider.get_page_list(path=url)
        i = 0
        while i<len(list):
            addDir(list[i][0], list[i][1])
            i = i + 1
        xbmcplugin.endOfDirectory(handle=handle, succeeded=True)
        
def playMp3(url):
    print "play mp3 = "+url
    xbmc.Player().play(item=url.replace(" ", "%20"))

params = parameters_string_to_dict(sys.argv[2])
_dir = sys.argv[2]
    
if len(_dir)==0:
    list_composers()
else:
    _dir = params.get("param")
    xbmc.log("_dir = "+_dir, level=xbmc.LOGNOTICE)
    if _dir.find("http")>=0:
        playMp3(_dir)
    else:
        load_page(_dir)
