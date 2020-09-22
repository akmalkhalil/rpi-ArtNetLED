import socket
from sys import argv as ARGV

class ArtNetNode(object):
    
    def __init__(self, ip, port):
        self.UDP_IP = ip
        # TODO: IP address validation
        self.PORT = port
        # TODO: make sure int is entered

        self.SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.SOCKET.bind((self.UDP_IP, self.PORT))

    
    def transmit(self, targIP, data, isBinary = True): # I wish I could do overloading so could have a bdata and ldata method
        if not isBinary:
            data = self._list2bin(data)
        


    def checkReceive(self, bufferSize = 1024, returnFrom = False): # TODO: better name
        if returnFrom:
            return self.SOCKET.recvfrom(bufferSize)
        else:
            return self.SOCKET.recv(bufferSize)
    
    def receive(self):
        raw = self.checkReceive()
        data = {
            "head" : raw[0:8],
            "opcode" : raw[8:10],
            "protocolHi" : raw[10:11],
            "protocolLo" : raw[11:12], # TODO: look up binary operations (things like >>>) and see if they're useable here
            "sequence" : raw[12:13],
            "physical" : raw[13:14],
            "universe" : raw[14:16],
            "lengthHi" : raw[16:17],
            "lengthLo" : raw[17:18],
            "bdata" : raw[18:530],
            "ldata" : self._bin2list(raw[18:530])
        }

        return data
    

    def _bin2list(self, binData):
        listdata = []
        for i in range(len(binData)):
            listdata.append(binData[i])
        return listdata
    def _list2bin(self, listData):
        pass




if __name__ == "__main__":
    node = ArtNetNode("192.168.0.71", 6454) # TODO: get IP from systems
    # For running on windows, python requires access through firewall
    artnetData = node.receive()
    print("DMX information recieved", artnetData["ldata"])

