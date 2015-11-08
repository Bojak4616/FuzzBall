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
    import sys
    import requests
    from requests import *    
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
        return r.status_code()

    def uaReq(self, UA, data):
        r = requests.get(self.url, headers=UA, data=data)
        return r.status_code()

class RandomDataGenerator():

    '''
        Name: RandomDataGenerator
        Purpose: Generating random text in a variety of languages 
                 to send to an end point. This should be used in conjunction
                 with the HTTPUtils in order to create unique body POST requests.
    '''

    def nepaliWords(self):
        fake = Factory.create('ne_NP')
        return fake.text()

    def turkishWords(self):
        fake = Factory.create('tr_TR')
        return fake.text()

    def chineseWords(self):
        fake = Factory.create('zh_CN')
        return fake.text()

if __name__ == "__main__":
    '''
        Test data generation
    '''

    url = "http://www.gentoocloud.com"
    data = "LOLOLOLOLOL"

    req = HTTPUtils(url)
    req.bodyReq(data)
