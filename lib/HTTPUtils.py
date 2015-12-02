#!/usr/bin/env python
'''
    Author: Jared Stroud

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:


    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.


    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
'''

try:
    import requests
    import random
    import sys
    from time import sleep
    from scapy.all import IP, TCP, send
except ImportError as err:
    print("Error " + str(err))
    sys.exit()

class HTTPUtils():

    '''
        Name: HTTPUtils
        Description: HTTP library used to create and manipulate requests to end points.
        Requirements: Python requests library.
    '''

    def __init__(self, URL):
        self.url = URL 

    def bodyReq(self, DATA):
        r = requests.post(self.url, data = DATA)
        return r

    def urlReq(self, data):
        r = requests.get(self.url, params=data)
        return r

    def uaReq(self, UA, data):
        r = requests.post(self.url, headers=UA, data=data)
        return r


class MalformHttpPacket():

    '''
        Name: malformPacket
        Purpose: Creates malformed packets to be fed into tshark
    '''
    def __init__(self, data):
        p = IP(src="127.0.0.1", dst="127.0.0.1")/TCP(dport=80)/str(data)
        self.packet = p

    def randomData(self):
        randData = ""
        methods = ['GET', 'OPTIONS', 'PUT', 'POST', 'HEAD', 'DELETE', 'TRACE']
        returns = '\r\n\r\n'

        for i in range(1, random.randrange(1, 120000)):
            randData += str(hex(random.randrange(0, 15)))[2:]

        if len(randData) % 2 != 0:
            randData += str(hex(random.randrange(0, 15)))[2:]

        data = methods[random.randrange(0, 6)] + ' ' + randData.decode('hex') + returns

        self.packet = IP(src="127.0.0.1", dst="127.0.0.1")/TCP(dport=80)/data
        return self.packet


if __name__ == "__main__":
    '''
        Sending weird payloaded packets of varying size over the wire.
        Start tell tshark to listen on loopback and congratz! you're kind of fuzzing
        ***Must run with sudo***

        More research needs to be done to get it to use the http dissector all the time.
        Invokes the http dissector about 50% of the time
    '''

    p = MalformHttpPacket("SEED")
    while(1):
        send(p.randomData())
        print "[+] Packet Sent"
        sleep(2)

