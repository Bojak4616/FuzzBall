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

    '''
        Name: __init__
        Purpose: constructor
        Parameters: self, self.pcap
            self.pcap: pcap to be operated on.
            
    '''
    def __init__(self, self.pcap):
        print("[+] Reading in " + str(self.pcap))

    '''
        Name: pcapReader
        Purpose: Read in pcap file.
        Parameters: self.pcap
            self.pcap: pcap to be operated on.
        Return: Nothing. Prints pcap line by line.
    '''
    def pcapReader(self, self.pcap):
        with PcapReader(str(self.pcap)) as pcap_reader:
            for pkt in pcap_reader:
                print("[+]>> " + str(pkt))


    

#TODO
# Read/write/hexdump functionality. Probably more things I haven't thought of yet.

if __name__ == "__main__":
	print("Running pcapRead...")
