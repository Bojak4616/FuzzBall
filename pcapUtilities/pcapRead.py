#!/usr/bin/env python

'''
Copyright (c) 2004 Dug Song <dugsong@monkey.org>
All rights reserved, all wrongs reversed.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

1. Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.
3. The names of the authors and copyright holders may not be used to
endorse or promote products derived from this software without
specific prior written permission.

THIS SOFTWARE IS PROVIDED ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES,
INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL
THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
 ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

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

class PRead:

    '''
    Name: pcapRead
    Purpose: Read in pcap file for future
    modification and protocol specific dissection.

    Some methods were taken from the dpkt Python module example Github repo.
    Source: https://raw.githubusercontent.com/kbandla/dpkt/master/examples/print_packets.py
    '''
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
        """
            Example taken from: https://raw.githubusercontent.com/kbandla/dpkt/master/examples/print_packets.py
           Print out information about each packet in a pcap

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
