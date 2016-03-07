__author__ = 'Philip'

import lib.HTTPUtils
import unittest

class TestHttpUtils(unittest.TestCase):
    def test_ReadEvilStrings(self):
        expectedEvilStrings = ['<script>alert(1)</script>`']
        httpUtils = lib.HTTPUtils.RawHTTPUtils('localhost', 8000)
        evilStrings = httpUtils.readEvilStrings('EvilStrings.txt')
        self.assertEqual(expectedEvilStrings, evilStrings)

    def test_HttpUtils(self):
        httpUtils = lib.HTTPUtils.RawHTTPUtils('localhost', 8000)
        self.assertEqual('localhost', httpUtils.addr)
        self.assertEqual('Fuzzball v1', httpUtils.host)
        self.assertEqual(8000, httpUtils.port)

    def test_HttpGet(self):
        expectedLog = 'HTTP/1.0 404 File not found'
        stringContained = False
        httpUtils = lib.HTTPUtils.RawHTTPUtils('localhost', 8000)
        httpUtils.rawGet()
        with open('Fuzzer.log') as fin:
            stringList = fin.readlines()
        if any(expectedLog in s for s in stringList):
            stringContained = True
        self.assertTrue(stringContained, "Expected string not contained in log")
        with open('Fuzzer.log', "w"):
            pass

    def test_StringGet(self):
        expectedLog = 'HTTP/1.0 404 File not found'
        stringContained = False
        httpUtils = lib.HTTPUtils.RawHTTPUtils('localhost', 8000)
        httpUtils.stringGet()
        with open('Fuzzer.log') as fin:
            stringList = fin.readlines()
        if any(expectedLog in s for s in stringList):
            stringContained = True
        self.assertTrue(stringContained, "Expected string not contained in log")
        with open('Fuzzer.log', "w"):
            pass

if __name__ == '__main__':
    unittest.main()