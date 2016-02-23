#!/usr/bin/python2.7

try:
    import sys
    import time 
except ImportError as err:
    print("[Error] Package missing %s" % (err))
    sys.exit()

class Log():

    def __init__(self):
        '''
            self.CloudLog: Log file for all actions.
            self.DropperLog: Log file for dropper (ansible).
            self.BeaconLog: Log file for beaconing logs (ansible).
        '''
        self.LogFile = "Fuzzer.log"

    def LogContent(self, file2log, contents):
        '''
            File to log contents to.
        '''
        with open(file2log, 'a+') as fout:
            fout.write("%s : %s \n" %(time.asctime(), contents))
        fout.close()

    def FuzzerLog(self, content):
        '''
            Name: CloudLog.
            Purpose: Log content to Cloud.log
            Return: Nothing.
        '''
        self.LogContent(self.LogFile, content)

    def ClearLog(self, file2log):
        with open(file2log, 'w') as fout:
            fout.write("")
        fout.close()

if __name__ == "__main__":
    testLog = Log()
    testLog.FuzzerLog("Stuff and things.")
