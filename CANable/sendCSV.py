import socket
import time
import sys
import packet 
sock = socket.socket(socket.PF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
sock.bind(("can0",))
if(len(sys.argv) !=2):
    print("Usage:sendCSV file.csv")
    sys.exit()
file = sys.argv[1]
inlines = list()
count =0
with open(file) as f:
    f.readline()
    inlines = f.readlines()
    for line in inlines:
        p = packet.Packet()
        p.initFromCSV(line)
        if(p.valid):
            p.sendPacket(sock)
            time.sleep(0.05)
            print(count)
            count += 1

