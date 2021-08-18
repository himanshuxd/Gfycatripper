#!/usr/bin/env python
from __future__ import unicode_literals
import youtube_dl
import argparse
import requests

__author__ = "Himanshu S"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "himanshuxd"

parser = argparse.ArgumentParser(description='Get all Gfycat Videos for a User')
parser.add_argument('foo')
args = parser.parse_args()

r = requests.get('https://api.gfycat.com/v1/users/'+args.foo+'/gfycats?count=200')

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	for gfy in r.json()['gfycats']:
		ydl.download(["https://www.gfycat.com/{}".format(gfy['gfyId'])])
