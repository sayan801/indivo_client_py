# tested with python 2.7.1
import argparse

parser = argparse.ArgumentParser(description="An argparse example")

parser.add_argument('action', help='The action to take (e.g. install, remove, etc.)')
parser.add_argument('foo-bar', help='Hyphens are cumbersome in positional arguments')

args = parser.parse_args()

if args.action == "install":
    print "You asked for installation"
else:
    print "You asked for something other than installation"
