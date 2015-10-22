'''
    Name: pcapRead
    Purpose: Read in pcap file for future
    modification and protocol specific dissection.

'''
try:
	import sys
	import scapy
except ImportError as err:
	print("[-] Cannot find package %s. Exiting", err)
	sys.exit()

__author__ = 'Jared'

class PRead:

    def __init__(self):
        print("[+] Pread object created.")


#TODO
# Read/write/hexdump functionality. Probably more things I haven't thought of yet.

if __name__ == "__main__":
	print("Running pcapRead...")
