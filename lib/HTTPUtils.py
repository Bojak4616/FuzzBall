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
    import os
    import sys
    import requests
    from requests import *    
    from faker import Factory
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

    def urlReq(self, data):
        r = requests.get(self.url, params=data)
        return r

    def uaReq(self, UA, data):
        r = requests.post(self.url, headers=UA, data=data)
        return r

class RandomDataGenerator():

    '''
        Name: RandomDataGenerator
        Purpose: Generating random text in a variety of languages 
                 to send to an end point. This should be used in conjunction
                 with the HTTPUtils in order to create unique body POST requests.

        Use-case: Can be used to test unicode support against web application. 
    '''

    def nepaliWords(self):
        '''
            Generating Nepal paragraphs.
        '''
        return Factory.create('ne_NP').text()

    def turkishWords(self):
        '''
            Generating Turksih paragraphs.
        '''
        return Factory.create('tr_TR').text()

    def chineseWords(self):
        '''
            Generating Chinese paragraphs.
        '''
        return Factory.create('zh_CN').text()

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
    url = "http://www.comecloserto.me" #Jesbags website :Dj
    rand = RandomDataGenerator()
    req = HTTPUtils(url)

    req.bodyReq(rand.nepaliWords())
    req.bodyReq(rand.turkishWords())
    req.bodyReq(rand.chineseWords())

    req.urlReq(rand.nepaliWords())
    req.urlReq(rand.turkishWords())
    req.urlReq(rand.chineseWords())

#    Must refactor code below. Erors
#    req.uaReq(rand.nepaliWords(), "")
#    req.uaReq(rand.turkishWords(), rand.turkishWords())
    req.uaReq(rand.chineseWords(), rand.chineseWords())

