#!/usr/bin/env python
__author__ = 'Jared'

class evalCmd:

    def cmdCheck(self, commandToEvaluate):

        if commandToEvaluate == "quit":
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
            print("TODO: implement loading of PCAP")

        elif commandToEvaluate == "parse":
            print("TODO: implement parsing")

        elif commandToEvaluate == "wireshark":
            print("TODO: launch wireshark with loaded pcap")
        else:
            print("Invalid command. Try typing help")

if __name__ == "__main__":
    print("Welcome to fuzzball, shall we begin?")
    test = evalCmd()
    while True:
        command = raw_input(">> ")
        try:
            test.cmdCheck(command)
        except ValueError as err: 
            print("Sorry, couldn't perform operation.")


