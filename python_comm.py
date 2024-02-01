import argparse
from pythonosc import dispatcher 
from pythonosc import osc_server 
from pythonosc import udp_client

# This script receives OSC messages from pd, uses them as parameters in pyhton functions
# and sends functions' output back as OSC messages. It is an ideal tool to process
# information comming from puredata's GUI (or any software that runs OSC) to take advanatge
# of python's robust infrastructure (i.e. running ML/generative processes) and then sending 
# information back in order to take advantage of pd's audio and MIDI processing and output.
#
# Your functions are run every time an OSC message arrives from pd. 
# OSC messages contain an address (a string preceded by "/") followed by a float or a list.
# The address in pd's message and the function's name must be the same (i.e "/myfunction2" 
# and "myfunction2()"). The last line of your functions should run "talk2pd()" and its 
# last parameter must be the message you want to send back to pd (only tuples). 
# For convenience, the address in the outgoing message to pd is also the same as the 
# incomming address and the function that is triggered.
#
# To create a new function:
# - the name of the function must coincide with the address sent from pd
#   (i.e. function name: "myfunction()"; message in pd: "set myfunction, $1")
# - your function should be run in the listen2pd() function below 
#   (see lines 62 and 63 where process1() and porocess2() are run)

# set input and output port numbers
input_port = 5005
output_port = 5006
###############################################################
###### functions where input from puredata is processed #######
###############################################################
def myfunction1(address, *message):
    print (address, message)
    a = message
    b = (a[0]**2)
    talk2pd(args.ipIN, args.portOUT, address, b)

def myfunction2(address, *message):
    print (address, message)
    a = message
    b = a[0]+1
    talk2pd(args.ipIN, args.portOUT, address, (b,1,b, 2,b,3,b,4))

###############################################################
###################### server functions #######################
###############################################################

def main(path: str, *osc_arguments):
    msg = osc_arguments[-1]

def listen2pd(addrIN,addrOUT):
    ipIN   = addrIN[0]
    portIN = addrIN[1]
    pathIN = addrIN[2]
    disp = dispatcher.Dispatcher()
    disp.map(pathIN, main, ipIN)
    
    ###############################################################
    ############ call functions that use data from pd ############
    ###############################################################
    # handlers are functions we want to run with pd information
    disp.map(address = "/myfunction1", handler = myfunction1) 
    disp.map(address = "/myfunction2", handler = myfunction2) 
    ###############################################################

    # server to listen
    server = osc_server.ThreadingOSCUDPServer((ipIN,portIN), disp)
    print("listening on {}".format(server.server_address))
    server.serve_forever()

def talk2pd(ip,port,path,mymove):
    client = udp_client.SimpleUDPClient(ip,port)
    #print (type(mymove))
    client.send_message(path, mymove)

if __name__ == "__main__":
    # generate parser
    parser = argparse.ArgumentParser(prog='python_comm', formatter_class=argparse.RawDescriptionHelpFormatter, description='Receive and send OSC messages from pd')
    parser.add_argument("-II","--ipIN", type=str, default="127.0.0.1", help="The ip to listen on")
    parser.add_argument("-PI", "--portIN", type=int, default=input_port, help="The port to listen on")
    parser.add_argument("-UI", "--uripathIN", type=str, default="/filter", help="PD's URI path")
    parser.add_argument("-PO", "--portOUT", type=int, default=output_port, help="The port to send messages to")
    parser.add_argument("-UO", "--uripathOUT", type=str, default="/filter", help="output URI path")
    args = parser.parse_args()
    # wrap up inputs
    outputAddress = [args.portOUT, args.uripathOUT]
    inputAddress = [args.ipIN, args.portIN, args.uripathIN]
    # listen
    listen2pd(inputAddress, outputAddress)
    
