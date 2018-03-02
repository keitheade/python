#!/usr/bin/python
'''
A simple program that will take a CIDR ip address as an argument or an input and give you:
CIDR
Network address
Subnetmask
First usable address
Last usable address
Broadcast address
'''
import os, sys, netaddr

def cls():
    os.system("clear")

def printip(ipcidr):
    cls()
    firststr = ("Input IP Address   : %s" % ipcidr)
    print firststr
    print(len(firststr)*"-")
    print("IP Address in CIDR : %s" % ipcidr.cidr)
    print("IP Network address : %s" % ipcidr.network)
    print("IP Subnet mask     : %s" % ipcidr.netmask)
    print("First IP address   : %s" % ipcidr[1])
    print("Last IP address    : %s" % ipcidr[-2])
    print("Broadcast address  : %s" % ipcidr[-1])

def setcidr():
    while True:
        print("Please enter an IP Network in CIDR notation, eg 127.0.0.1/24  'Exit' to quit")
        ip = raw_input(":> ")
        if ip == "Exit" or ip == "exit":
            exit(-1)
        if ( raw_input("Is this %s correct?   y/n\n:> " %ip) == 'y'):
            printip(netaddr.IPNetwork(ip))
            raw_input()

if len(sys.argv)>1:
    ipcidr = netaddr.IPNetwork(sys.argv[1])
    printip(ipcidr)
else:
    while True:
        setcidr()
