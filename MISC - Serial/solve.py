import socket
import re

flag = ""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("misc.chal.csaw.io", 4239))

def xor(d):	
	total = 0
	for i in range(0,len(d)):
		total = total ^ int((d[i]))
	return total


while 1:
	data = s.recv(1024)
	data = data.replace("\n","")
	if "8-1-1" in data:
		data = data.replace("8-1-1 even parity. Respond with '1' if you got the byte, '0' to retransmit.","")
	if data == "":
	    break
	print "Received:", repr(data)
	extracted = data[1:-1]
	print "Extracted:",extracted
	x = xor(extracted)
	print "xor : ", x
	if x == 0:
		s.sendall("1")
		flag += str(data[1:-2])
	else:
		s.sendall("0")
	data = None

print flag
print "Connection closed."
s.close()
