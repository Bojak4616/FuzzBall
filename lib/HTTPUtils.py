#!/usr/bin/python2.7
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

import os
import sys
import socket

class RawHTTPUtils():
    '''
        Name: RawHTTPUtils
        Description: HTTP requests using only socket.
        Requirements: Socket.
    '''
    def __init__(self, address, port):
        self.addr = str(address)
        self.port = int(port)
        self.host = "Fuzzball v1"

        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.addr, self.port))
        except socket.error as msg:
            print("[ERROR] %s " % msg)
            sys.exit(0)

    def readEvilStrings(self, stringFile="EvilStrings.txt"):
        '''
            Name: readEvilStrings
            Parameters: stringFile: Where the evil strings are kept.
            Return: List of strings.
        '''
        with open(stringFile) as fin:
            stringList = fin.readlines()

        return (stringList)

    def rawGet(self, data="/index.html"):
        '''
            Name: rawGet
            Description: GET request using sockets.
            Parameters: string value (data)
        '''
        self.sock.send('GET %s HTTP/1.1\r\nHost: %s\r\n\r\n' % (data, self.host))

    def stringGet(self):
        '''
            Name: stringGet
            Parameters: self.
            Return: Nothing
        '''
        evilContents = self.readEvilStrings()

        for data in evilContents:
            print("[+] Sent %s to %s" % (data, self.addr))
            self.rawGet(data)

    def rawHead(self):
        '''
            Name: rawHead
            Description: rawHead request using sockets.
            Parameters: None.
        '''
        self.sock.send("HEAD HTTP/1.1\r\nHost: %s\r\n\r\n" % self.host)

    def rawPost(self):
        '''
            Name: rawPost
            Description: rawHead request using sockets
            Parameters: None.
        '''
        headers = """\
        POST /auth HTTP/1.1\r
        Content-Type: {content_type}\r
        Content-Length: {content_length}\r
        Host: {host}\r
        Connection: close\r
        \r\n"""

        body = 'username=Fuzz&password=Pass'
        body_bytes = body.encode('assci')
        header_bytes = headers.format(
            content_type="application/x-www-form-urlencoded",
            content_length=len(body_bytes),
            host=self.addr + ":" + self.port
        ).encode('iso-8859-1')

        payload = header_bytes +  body_bytes
        self.sock.sendall(payload)

class RandomDataGenerator():
    '''
        Name: RandomDataGenerator
        Purpose: Generating random text in a variety of languages 
                 to send to an end point. This should be used in conjunction
                 with the HTTPUtils in order to create unique body POST requests.

        Use-case: Can be used to test unicode support against web application. 
    '''

    def devRand(self, numBytes=50):
        '''
            Portable way to return random bytes.
            Linux/Unix uses /dev/urandom
            Windows: CryptGetRandom()
        '''
        return os.urandom(numBytes)


if __name__ == "__main__":
    '''
        Test data generation
    '''
    url = "localhost" 
    req = RawHTTPUtils(url, 8000)
    #req.rawHead()
    req.stringGet()
