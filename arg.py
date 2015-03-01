import sys, string, os

length = len(sys.argv)

print "Parameters: %s"%length

if length != 3 :
    raise Exception("Pass Username and password as argument")

user = sys.argv[1]

print "Indivo User: %s"%user

password = sys.argv[2]

print "Indivo Password: %s"%password

