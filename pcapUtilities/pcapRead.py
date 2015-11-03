#!/usr/bin/env python
'''
    Name: pcapRead
    Purpose: Read in pcap file for future
    modification and protocol specific dissection.

'''
try:
        import socket
        import datetime
	import sys
        import dpkt
        from scapy import *
        from pcapfile import savefile
except ImportError as err:
    print("[-] Cannot find package: " + str(err))
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
        print("[+] PRead object created") 

    '''
        Name: pcapReader
        Purpose: Read in pcap file.
        Parameters: self.pcap
            pcap: pcap to be operated on.
        Return: whole packet as a list.
    '''
    def pcapReader(self, pcap):
        testcap = open(str(pcap))
        capfile = savefile.load_savefile(testcap, verbose=True)
        print capfile

        return capfile


    def ip_to_str(self, address):
        return socket.inet_ntop(socket.AF_INET, address)

    def mac_addr(self, mac_string):
        return ':'.join('%02x' % ord(b) for b in mac_string)

    def print_packets(self, pcap):
        """Print out information about each packet in a pcap

           Args:
               pcap: dpkt pcap reader object (dpkt.pcap.Reader)
        """
        # For each packet in the pcap process the contents
        for timestamp, buf in pcap:

            # Print out the timestamp in UTC
            print 'Timestamp: ', str(datetime.datetime.utcfromtimestamp(timestamp))

            # Unpack the Ethernet frame (mac src/dst, ethertype)
            eth = dpkt.ethernet.Ethernet(buf)
            print 'Ethernet Frame: ', self.mac_addr(eth.src), self.mac_addr(eth.dst), eth.type

            # Make sure the Ethernet frame contains an IP packet
            # EtherType (IP, ARP, PPPoE, IP6... see http://en.wikipedia.org/wiki/EtherType)
            if eth.type != dpkt.ethernet.ETH_TYPE_IP:
                print 'Non IP Packet type not supported %s\n' % eth.data.__class__.__name__
                continue

            # Now unpack the data within the Ethernet frame (the IP packet) 
            # Pulling out src, dst, length, fragment info, TTL, and Protocol
            ip = eth.data

            # Pull out fragment information (flags and offset all packed into off field, so use bitmasks)
            do_not_fragment = bool(ip.off & dpkt.ip.IP_DF)
            more_fragments = bool(ip.off & dpkt.ip.IP_MF)
            fragment_offset = ip.off & dpkt.ip.IP_OFFMASK

            # Print out the info
            print 'IP: %s -> %s   (len=%d ttl=%d DF=%d MF=%d offset=%d)\n' % \
                  (self.ip_to_str(ip.src), self.ip_to_str(ip.dst), ip.len, ip.ttl, do_not_fragment, more_fragments, fragment_offset)

    '''
        Name: pcapHexDump
        Purpose: Read in pcap file and print out a hexdump.
        Parameters: self, pcap
            pcap: pcap to be operated on.
        Return: returns hexdump of pcap operated on.
    '''

    def pcapHexDump(self, pcap):
        with open(pcap) as f:
            rpcap = dpkt.pcap.Reader(f)
            self.print_packets(rpcap)
        
#TODO
# Read/write/hexdump functionality. Probably more things I haven't thought of yet.

if __name__ == "__main__":
	print("Running pcapRead...")
