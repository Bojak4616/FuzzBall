#!/usr/bin/python2.7
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

__author__ = "Jared E. Stroud, Jon Meyers"

try:
    import sys
    import argparse 
    import random
    import threading
    from lib.HTTPUtils import RawHTTPUtils
except ImportError as error:
    print("Error is %s" % error)
    sys.exit()

class cmdEval:
    '''
        Name: cmdEval
        Purpose: Evaluating user arguments and calling associated methods.
    '''

    def fuzzCall(self, usrCmd, address, fuzzData, port):
        '''
            Name:fuzzCall
            Parameters: usrCmd (user specified command)
                        address (ip address)
                        fuzzData (data to send)
        ''' 
        fuzzHTTP = RawHTTPUtils(str(address), int(port))
        command = { 
                    "http" :  fuzzHTTP.rawGet(fuzzData)
                  }

        if usrCmd.lower() not in command.keys(): # If the user supplied argument does not exist as a key, quit.
            print("Function %s does not exist!\n" % usrCmd)
            sys.exit()
        else:
           cmdResult = command.get(str(usrCmd))
        return cmdResult

if __name__ == "__main__":

    cmd = cmdEval()
    parser = argparse.ArgumentParser()
    parser.add_argument("--dst", nargs=1, required=False,  help="Specify the destination address") 
    parser.add_argument("--identify", required=False,  help="Attempt to profile a web server.") 
    parser.add_argument("--port", nargs=1, required=False,  help="Specify the destination port", default=80) 
    parser.add_argument("--fuzz", nargs=1, required=False, help="Specify the protocol to Fuzz(Ex: HTTP, FTP)")
    parser.add_argument("--data", nargs=1, required=False, help="Specify the data to be sent")
    parser.add_argument("--threads", nargs=1, required=False, help="Specify the number of threads to Fuzz with.", default=1)
    args = parser.parse_args()

    ### Identifiying user given commands.
    if (args.identify and args.dst):
        print("[+] Profiling webserver")
        sys.exit()
    elif args.dst and args.fuzz:
        data = ''.join(args.data) # Removes list bindings.
        dst =  ''.join(args.dst)  # Removes list bindings.
        fuzz = ''.join(args.fuzz) # Removes list bindings.
        port = ''.join(args.port) # Removes list bindings.
        if args.threads == 1:
            threads = ''.join(str(args.threads))
        else:
            threads = ''.join(args.threads)

        print ("[+] Destination is : %s\n"\
               "[+] Scan running is : %s\n"\
               "[+] Data being sent is : %s\n"\
               "[+] Destination Port is : %s\n"\
               "[+] Number of Threads used is : %s\n" % (dst, fuzz, data, port, threads))
        try:
            #cmd.fuzzCall(fuzz, dst, data, int(port))
            for i in range(int(threads)):
                t = threading.Thread(target=cmd.fuzzCall, args=(fuzz, dst, data, int(port)))
                t.start()

        except ValueError,e:
            print("[-] Error, incorrect syntax.\nTry ./Fuzzer -h.\n"\
                 "./Fuzzer --dst http://localhost --fuzz http --data lolcakes")
            print(str(e))
    else:
        print("[-] Error, I didn't understand what you wanted to do!")
        sys.exit()
