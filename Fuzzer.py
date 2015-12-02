#!/usr/bin/env python
'''
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

__author__ = "Jared E. Stroud"

try:
    import subprocess
    import sys
    import argparse
    import logging
    logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
    from lib.HTTPUtils import *
    from time import ctime
except ImportError as error:
    print("Error is " + str(error))
    sys.exit()

class cmdEval:
    '''
        Name: cmdEval
        Purpose: Evaluating user arguments and calling associated methods.
    '''

    def fuzzCallHTTP(self, usrCmd, address, fuzzData):

        fuzzHTTP = HTTPUtils(str(address))

        command = { 
                    "http" :  fuzzHTTP.urlReq(str(data))
                  }

        if usrCmd.lower() not in command.keys(): #If the user supplied argument does not exist as a key, quit.
            print("Function " + str(usrCmd) + " does not exist!")
            sys.exit()
        else:
           cmdResult = command.get(str(usrCmd))
        return cmdResult

    def fuzzTshark(self, fuzz, data):
        p = subprocess.Popen(['tshark', '-i', 'lo0'])
        pid = p.pid

        if fuzz == 'HTTP':
            packet = MalformHttpPacket(data)
            try:
                while True:
                    send(packet.randomData(), verbose=False)
                    if pid != p.pid:
                        p = subprocess.Popen(['tshark', '-i', 'lo0'])
                        pid = p.pid

                        filename = str(ctime()) + " BadPacket.pcap"
                        with open(filename, 'w') as f:
                            f.write(packet.packet)

            except KeyboardInterrupt as e:
                print e
                sys.exit()




if __name__ == "__main__":
    cmd = cmdEval()
    parser = argparse.ArgumentParser()
    parser.add_argument("--dst",  nargs=1, required=True, help="Specify the destination address or 127.0.0.1 for tshark")
    parser.add_argument("--fuzz", nargs=1, required=True, help="Specify the protocol to Fuzz(Ex: HTTP)")
    parser.add_argument("--data", nargs=1, required=True, help="Specify the data to be sent or a seed for tshark")
    args = parser.parse_args()
    """Sample Commandline: sudo ./Fuzzer.py --dst 127.0.0.1 --fuzz HTTP --data seed"""

    if args.dst and args.fuzz:
        data = ''.join(args.data) #Removes list bindings.
        dst  = ''.join(args.dst)  #Removes list bindings.
        fuzz = ''.join(args.fuzz) #Removes list bindings.

        print ("[+] Destination is : " + str(dst))
        print ("[+] Scan running is : " + str(fuzz))
        print ("[+] Data being sent is : " + str(data))

        if str(dst) == "127.0.0.1":
            cmd.fuzzTshark(fuzz, data)
        else:
            cmd.fuzzCallHTTP(fuzz, dst, data)
