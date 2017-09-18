import dpkt
import binascii

filename='cap.pcap'
data = ''
for ts, pkt in dpkt.pcap.Reader(open(filename,'r')):    
    eth=dpkt.ethernet.Ethernet(pkt) 
    ip=eth.data
    print ip
    tcp=ip.data
    
    if "&x=" in tcp.data:
	x = tcp.data.split("&x=")[1].replace("\n","")
	data += x

print data

text_file = open("pic.bmp", "wb")
text_file.write(binascii.unhexlify(data))
text_file.close()
