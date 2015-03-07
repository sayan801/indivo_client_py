#!/usr/bin/python

from client import IndivoClient
from xml.dom import minidom as XML

import xmltodict, json

import xml.etree.ElementTree as ET

import sys, string, os

length = len(sys.argv)

print "Parameters: %s"%length

if length != 4 :
    raise Exception("Usage: Python Filename record_id consumer_key consumer_secret")

record_id = sys.argv[1]

print "record_id: %s"%record_id

consumer_key = sys.argv[2]

print "consumer_key: %s"%consumer_key

consumer_secret = sys.argv[3]

print "consumer_secret: %s"%consumer_secret


# Need to pass these in to the client
SERVER_PARAMS = {"api_base": "http://login.mycuratio.com:8000",
                 "authorization_base": "http://login.mycuratio.com"}

CONSUMER_PARAMS = {"consumer_key": consumer_key,
                   "consumer_secret": consumer_secret}

# Set up the client (with no token): two-legged oauth only
#client = IndivoClient(SERVER_PARAMS, CONSUMER_PARAMS)
client = IndivoClient(SERVER_PARAMS, CONSUMER_PARAMS, pha_email=CONSUMER_PARAMS["consumer_key"])

resp, content = client.smart_allergies(record_id = record_id )

print "Response Details: %s\n"%resp

print "%s"%content

o = xmltodict.parse(content)

print "%s"%json.dumps(o)

#tree = ET.fromstring(content or '<Account/>')
#if tree is not None:
# record_id = tree.attrib.get('id')
# print "Record id %s "%record_id
