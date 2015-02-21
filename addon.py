import os
import sys
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
from classical import OneClassical

__plugin__ = "plugin.audio.oneclassical"
__author__ = "pinoelefante"

Addon = xbmcaddon.Addon(id=__plugin__)

handle = int(sys.argv[1])

provider = OneClassical()
list = provider.get_composer_list()
i = 0
while i<len(list):
    item = list[i]
    li = xbmcgui.ListItem(label=item[0], iconImage=None)
    xbmcplugin.addDirectoryItem(handle=handle, url=item[1], listitem=li)
    #print item[0] + " "+ item[1]
    i = i + 1
xbmcplugin.endOfDirectory(handle=handle, succeeded=True)