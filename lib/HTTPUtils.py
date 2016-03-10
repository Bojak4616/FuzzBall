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
        self.buff = 4096
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.addr, self.port))
        except socket.error as msg:
            print("[ERROR] %s " % msg)
            sys.exit(0)

    def rawGet(self, data="/index.html", host="www.example.com"):
        '''
            Name: rawGet
            Description: GET request using sockets.
            Parameters: 
                data: URI
                host: Originating host

            Return: Contents of GET response.
        '''
        self.sock.send('GET %s HTTP/1.1\r\nHost: %s\r\n\r\n' % (data, host))
        return self.sock.recv(self.buff)
        self.sock.close()

    def rawHead(self, host="example.com"):
        '''
            Name: rawHead
            Description: rawHead request using sockets.
            Parameters: None.
            Return: Result of HEAD request.
        '''
        self.sock.send("HEAD HTTP/1.1\r\nHost: %s\r\n\r\n" % host)
        return self.sock.recv(self.buff)
        self.sock.close()

    def rawPost(self, PostURI="/", contentType="Accept: text/plain", contentLen= "9001", bodyContents="Username:Testing", host="example.com"):
        '''
            Name: rawPost
            Description: Raw socket post library.
            Parameters:
                PostURI: Specify URI.
                contentType: Specicy content type.
                contentLen: Specify content length.
                bodyContents: Specify body payload of HTTP POST request.
                host: Specify origin host.
            Return: Response contents of HTTP POST.
        '''

        headers = """\r
        POST /%s HTTP/1.1\r
        Content-Type: %s\r
        Content-Length: %s\r
        Host: %s\r
        Connection: close\r
        \r\n""" % (PostURI,contentType, contentLen, host)

        body = bodyContents
        body_bytes = body.encode('ascii')

        header_bytes = headers.format(
            content_type="application/x-www-form-urlencoded",
            content_length=len(body_bytes),
            host=self.addr + ":" + str(self.port)
        ).encode('iso-8859-1')

        payload = header_bytes +  body_bytes
        self.sock.sendall(payload)

        return self.sock.recv(self.buff)
        self.sock.close()

if __name__ == "__main__":
    '''
        Test data generation
    '''
    url = "localhost" 
    req = RawHTTPUtils(url, 8000)
    #req.rawGet("/", "localhost")
    #print(req.rawHead(host="chaimsanders.com"))
    #print(req.rawPost(host="localhost"))
