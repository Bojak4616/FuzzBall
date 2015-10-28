#!/usr/bin/env python
__author__ = 'Jared'

try:
    import os
    from pcapUtilities.pcapRead import PRead
except ImportError as err:
    print("Error, cannot find package " + err)

pread = PRead()

class evalCmd:

    def __init__(self):
        self.pcapLoaded = 0 # Variable for determining if a pcap has been loaded.

    '''
        Function: cmdCheck
        Parameters:self, commandToEvaluate
            self: Required by the class.
            commandToEvaluate: User input that then compares it to available commands and launches
                               additional methods.

        Return: Nothing, prints status of current funcionality, and (TODO) calls other method.
    '''
    def cmdCheck(self, commandToEvaluate):

        if commandToEvaluate == "quit" or commandToEvaluate == "exit":
            import sys
            sys.exit()

        elif commandToEvaluate == "help":
            print("""
                    load: load a pcap for operations to be performed on.
                    parse: parse a loaded pcap.
                    wireshark: launch modified pcap in wiresharl.
                    help: launch this program.
                    quit: exit the program.
                  """)
        
        elif commandToEvaluate == "load":
            self.pcapToLoad = raw_input("Enter name of pcap: ")
            pread.pcapReader(self.pcapToLoad)
            self.pcapLoaded = 1 #Pcap has been loaded. Requried for wireshark functionality.

        elif commandToEvaluate == "parse":
            print("TODO: implement parsing")
        elif commandToEvaluate == "wireshark":

            if self.pcapLoaded == 1: 
                print("Loading packet: " + self.pcapToLoad)
                os.system("wireshark " + self.pcapToLoad)
            else:
                print("No pcap loaded...")
        else:
            print("Invalid command. Try typing help")


if __name__ == "__main__":
    print("Welcome to fuzzball, shall we begin?")
    usrCmd = evalCmd()
    while True:
        command = raw_input(">> ") 
        try:
            usrCmd.cmdCheck(command)
        except ValueError as err: 
            print("Sorry, couldn't perform operation.")
