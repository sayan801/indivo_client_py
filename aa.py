from client import IndivoClient
from xml.dom import minidom as XML

import sys, string, os

length = len(sys.argv)

print "Parameters: %s"%length

if length != 3 :
    raise Exception("Pass Username and password as argument")

user = sys.argv[1]

print "Indivo User: %s"%user

password = sys.argv[2]

print "Indivo Password: %s"%password

# Need to pass these in to the client
SERVER_PARAMS = {"api_base": "http://login.mycuratio.com:8000",
                 "authorization_base": "http://login.mycuratio.com"}
CONSUMER_PARAMS = {"consumer_key": "curatehealth",
                   "consumer_secret": "curatehealth"}

# If we already had a token (access token, request token, or session token), it should be formatted
# like this. We won't use this in the example.
RESOURCE_TOKEN = {"oauth_token": "asdfdsfa",
                  "oauth_token_secret": "adfasdf"}

# Set up the client (with no token): two-legged oauth only
client = IndivoClient(SERVER_PARAMS, CONSUMER_PARAMS)
#, pha_email=CONSUMER_PARAMS["consumer_key"])

# make the get_version call, and print it out
resp, content = client.get_version(body={'a':'b', 'c':'d'})
if resp['status'] != '200':
    raise Exception("Bad Status: %s"%resp['status'])
print "Indivo Version: %s"%content



resp, content = client.session_create({'username' : user , 'password' : password})
print "Session info: %s"%content
print "Session_info Response object looks like: %s"%resp
   
