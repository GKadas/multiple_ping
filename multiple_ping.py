import os
import sys
import subprocess

print (sys.version)
# I can improve this so bad!!!!

type_of = raw_input("Scan based on (ip or host):")

while type_of not in ('host', 'ip'):
    print("Not acceptable input")
    type_of = input("Scan based on (ip or host):")


if type_of == 'host':
    with open('hosts.txt') as f: lines = f.read().splitlines()
    for line in lines:
        hostname = str(line)
        response = subprocess.call(['ping', hostname])
        if response == 0:
            print "ping to", hostname, "OK"
        elif response == 2:
            print "no response from", hostname
        else:
            print "ping to", hostname, "failed!"
else:
    with open('ip.txt') as f: lines = f.read().splitlines()
    for line in lines:
        address = str(line)
        response = subprocess.call(['ping', address])
        if response == 0:
            print "ping to", address, "OK"
        elif response == 2:
            print "no response from", address
        else:
            print "ping to", address, "failed!"

