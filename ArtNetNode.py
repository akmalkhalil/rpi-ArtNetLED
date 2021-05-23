import socket
from sys import argv as ARGV
from datetime import datetime

class ArtNetNode(object):
    
    def __init__(self, ip, port, testing = False, listenBroadcast = False):
        self.UDP_IP = ip
        # TODO: IP address validation
        self.PORT = port
        # TODO: make sure an int is entered
        self.testing = testing # I really don't know about this, I just added it so that I could run tests on methods without messing with ports and stuff on windows
        
        if not testing:
            self.SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            if listenBroadcast:
                self.SOCKET.bind(("", self.PORT)) # Listen to artnet packets that are broadcasted on the network
                # TODO: This is currently noisy and needs looking in to
            else:
                self.SOCKET.bind((self.UDP_IP, self.PORT))

    
    def transmit(self, targIP, data, isBinary = True): # I wish I could do overloading so could have a bdata and ldata method
        if not isBinary:
            data = self._list2bin(data)
            return 0
        


    def checkReceive(self, bufferSize = 1024, returnFrom = False): # TODO: better name
        if returnFrom:
            return self.SOCKET.recvfrom(bufferSize)
        else:
            return self.SOCKET.recv(bufferSize)
    
    def receive(self):
        print(self.UDP_IP, self.PORT, datetime.now().strftime("%H:%M:%S"))
        raw = self.checkReceive()
        data = {
            "head" : raw[0:8],
            "opcode" : raw[8:10],
            "protocolHi" : raw[10:11],
            "protocolLo" : raw[11:12], 
            "sequence" : raw[12:13],
            "physical" : raw[13:14],
            "universe" : raw[14:16],
            "lengthHi" : raw[16:17],
            "lengthLo" : raw[17:18],
            "bdata" : raw[18:530],
            "ldata" : self._bin2list(raw[18:530])
        }# TODO: look up binary operations (things like >>>) and see if they're useable here, and if they'll speed up a little

        return data
    
    # @param: a byte string, e.g. b'\x00\ff\x88'
    # @return: an int list containg each byte from the string
    def _bin2list(self, binData):
        # TODO: look into just using the list() method, I think that's all I need really
        listdata = []
        for i in range(len(binData)):
            listdata.append(binData[i])
        return listdata
    def _list2bin(self, listData):
        return bytes(listData)




if __name__ == "__main__":
#    hostname = socket.gethostname()
#    ipaddress = socket.gethostbyname(hostname)
#    print("IP Address:  ", ipaddress)
    node = ArtNetNode("192.168.0.51", 6454) # TODO: get IP from systems
    # For running on windows, python requires access through firewall
    artnetData = node.receive()
    print("DMX information recieved", artnetData["ldata"])

