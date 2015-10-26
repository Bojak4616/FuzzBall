#!/usr/bin/env python
'''
    Name: pcapRead
    Purpose: Read in pcap file for future
    modification and protocol specific dissection.

'''
try:
	import sys
        from scapy.all import *
except ImportError as err:
	print("[-] Cannot find package %s. Exiting", err)
	sys.exit()

__author__ = 'Jared'

class PRead:

    '''
        Name: __init__
        Purpose: constructor
        Parameters: self, self.pcap
            self.pcap: pcap to be operated on.
            
    '''
    def __init__(self):
        print("[+] object created") 

    '''
        Name: pcapReader
        Purpose: Read in pcap file.
        Parameters: self.pcap
            pcap: pcap to be operated on.
        Return: whole packet as a list.
    '''
    def pcapReader(self, pcap):

        preader = rdpcap(pcap)
        print(preader)

        return preader


    '''
        Name: pcapHexDump
        Purpose: Read in pcap file and print out a hexdump.
        Parameters: self, pcap
            pcap: pcap to be operated on.
        Return: returns hexdump of pcap operated on.
    '''
    def pcapHexDump(self, pcap):

        preader = rdpcap(pcap)
        print(hexdump(preader))

        return hexdump(preader)


    

#TODO
# Read/write/hexdump functionality. Probably more things I haven't thought of yet.

if __name__ == "__main__":
	print("Running pcapRead...")
