#!/usr/bin/python

from client import IndivoClient
from xml.dom import minidom as XML

import xml.etree.ElementTree as ET

import sys, string, os

length = len(sys.argv)

print "Parameters: %s"%length

if length != 8 :
    raise Exception("Usage: Python Filename Username password givenname familyname email gender dob")

user = sys.argv[1]

print "Indivo User: %s"%user

password = sys.argv[2]

print "Indivo Password: %s"%password

givenname  = sys.argv[3]
familyname  = sys.argv[4]
email  = sys.argv[5]
gender = sys.argv[6]
dob = sys.argv[7]

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
if resp['status'] != '200':
    raise Exception("Bad Status: %s"%resp['status'])
result =  dict(item.split("=") for item in content.split("&"))	
account_id =  result['account_id']

print "Account id %s "%account_id

xmlStart = '<Demographics xmlns="http://indivo.org/vocab/xml/documents#">'

demographics =  "%s<dateOfBirth>%s</dateOfBirth><gender>%s</gender><email>%s</email><Name><familyName>%s</familyName><givenName>%s</givenName></Name></Demographics>"%(xmlStart,dob,gender,email,familyname,givenname)

print "demographics :%s"%demographics

res, content = client.record_create(body=demographics)
status = res['status']

print "Record Create info: %s"%content

# success, parse XML and change owner to current user
if '200' == status:
	tree = ET.fromstring(content or '<Record/>')
	if tree is not None:
		record_id = tree.attrib.get('id')
		res, content = client.record_set_owner(record_id=record_id, body=account_id, content_type='text/plain')
		status = res['status']
		print "Record Set Owner info: %s"%content
		if '200' == status:
			print "Added record to: %s "%user
		else:
			print "Failed to add record to: %s "%user
	else:
		print "Record id not found: %s "%user
else:
	print "Failed Create record to: %s "%user


#print "Session info: %s"%content
#print "Session_info Response object looks like: %s"%resp
   
