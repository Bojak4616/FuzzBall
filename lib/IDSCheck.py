#!/usr/bin/env python
'''
    Author: Jared E Stroud
    purpose: IDS/IPS rule validator
'''

try:
    import requests
    import logging
    from scapy.all import *
    from datetime import datetime
    from scanner import bacnetNSE
    from utils import FuzzyLog
except ImportError as err:
    print("Error I don't have " + str(err))

idsLog = FuzzyLog()

class ruleCheck:

    '''
        Name: __init__
        Parameters:
            ruleFile: Used to specify where to read in IDS test strings.
    '''
    def __init__(self, ruleFile):
	self.testStrings = ruleFile

    '''
        Name: ruleRead()
        Purpose: Read in test strings to be fired against an IDS/IPS.
        Parameters: self
        Return: IDS test strings.
    '''
    def ruleRead(self):
        with open(self.testStrings, "r") as fin:
            lines = fin.readlines()

        return "".join(lines)  # Remvoing array brackets

    '''
        Name: ruleTest
        Purpose: Send test strings to IDS to trigger.
        Parameters: self, dstHost, dstPrt
            dstHost: Destination host to send packets to.
            dstPrt: Destination port
        Return: IDS test strings.
    '''
    def ruleTest(self, dstHost, dstPrt):
        dhost = str(dstHost)
        dport =  str(dstPrt)
        idsLog.amiroot()
        idsLog.amiroot()
        badstrings = self.ruleRead().split()

        for payload in badstrings:
            self.hailMerry(dhost, dport, payload)

    def hailMerry(self, dest, dpt, payload):
        data = str(payload)
        pkt = IP(dst=dest)/TCP(dport=int(dpt))/Raw(load=data)
        send(pkt)

if __name__ == "__main__":

    idsLog.fuzzyLog("Checking rule: ")
    rcheck = ruleCheck("rules.txt")

    print(rcheck.ruleTest("localhost", 80))
