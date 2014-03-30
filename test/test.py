__plugin__ = 'USTV VoD'
__authors__ = 'BlueCop'
__credits__ = 'moneymaker, slices, zero'
__version__ = '1.0.0'

import os
import sys
import importlib
import urllib
import operator
from urlparse import urlparse, parse_qs



# mock imports
os.sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "mock"))
import xbmcplugin
import xbmc
import xbmcgui
import xbmcaddon

__addon__ = xbmcaddon.Addon('plugin.video.ustvvod')

# add parent path for mdodules
os.sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
import resources.lib._common as common

# setup dummy varible
common.args.url = "URL"

# dummy method
def setView(view):
	return

# bucket for loading listings
bucket = []
def addDirectory(name, mode='', sitemode='', url='', thumb=False, fanart=False, description=False, aired='', genre='',count=0):
	bucket.append( {"name" : name, "url" : url, "sitemode" : sitemode, "network" : mode} )
	return
def addShow(name, network, sitemode, url):
	bucket.append( {"name" : name, "url" : url, "sitemode" : sitemode, "network" : network} )
	return

# list of videos
videos = []
def addVideo(u,displayname,thumb=False,fanart=False,infoLabels=False,HD=False):
	qs = parse_qs(urlparse(u).query)
	videos.append( {"name" : displayname, "url" : qs['url'][0][1:-1], "sitemode" : qs['sitemode'][0][1:-1], "network" : qs['mode'][0][1:-1]} )
	return

# monkey patch common
common.addDirectory = addDirectory
common.addShow = addShow
common.addVideo = addVideo
common.setView = setView



def ListItem(url, iconImage = "", thumbnailImage = ""):
	print "ADD LIST ITEM :: " + url
	return xbmcgui.MockListItem()

xbmcgui.ListItem = ListItem



def test_load_networks():
	print "Sanity check all modules load"
	common.get_networks()


def test_whitelist_only():
	whitelist = []
	with open("whitelist.txt") as f:
	    whitelist = f.read().splitlines()
	

	for whitelist_item in whitelist:
		if whitelist_item.startswith('#'):
			continue
		
		del bucket[:]	# empty page bucket
		del videos[:]	# empty videos
		print whitelist_item
		tree = whitelist_item.split('|');
		network = tree.pop(0)
		module = common.get_network(network)
		rootlist = module.rootlist() or bucket

		for tree_item in tree:
			for bucket_item in bucket:
				if bucket_item["name"] == tree_item:
					getattr(module, bucket_item['sitemode'])(bucket_item['url'])
					break

		for video in videos:
			print video["name"]
			print video
			getattr(module, video['sitemode'])(video['url'])


def test_all():
	for network in common.site_dict:
		module = importlib.import_module('resources.lib.%s' % (network))
		while len(bucket) > 0:
			item = bucket.pop()
			
			getattr(module, item['sitemode'])(item['url'])


#test_load_networks()
test_whitelist_only()







