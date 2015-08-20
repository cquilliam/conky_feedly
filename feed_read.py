#!/usr/bin/env python

from feedly import FeedlyClient
import json
from subprocess import call
from os.path import expanduser
import time

FEEDLY_REDIRECT_URI = "http://fabreadly.com/auth_callback"
FEEDLY_CLIENT_ID = "client_id"
FEEDLY_CLIENT_SECRET = "client_secret"

def get_feedly_client(token=None):
	if token:
		return FeedlyClient(token=token, sandbox=False)
	else:
		return FeedlyClient(
			client_id=FEEDLY_CLIENT_ID,
			client_secret=FEEDLY_CLIENT_SECRET,
			sanbox=False
		)

def auth(request):
	feedly = get_feedly_client()
	code_url = feedly.get_code_url(FEEDLY_REDIRECT_URI)
	return redirect(code_url)


def callback(request):
	code=request.GET.get('code','')
	if not code:
		return HttpResponse('The authentication is failed.')

	feedly = get_feedly_client()
	res_access_token = feedly.get_access_token(FEEDLY_REDIRECT_URI, code)
	if 'errorCode' in res_access_token.keys():
		return HttpResponse('The authentication is failed')

	id = res_access_token['id']
	access_token=res_access_token['access_token']
json_data=open(expanduser('~')+'/.conky/Feedly/settings.json')
data=json.load(json_data)
access_token=data['access_token']
category=data['category']
client = get_feedly_client(access_token)
content = client.get_feed_content(access_token,category,unreadOnly=True)
for item in content['items']:
  print ("${color1}%s" %(item['title']))
