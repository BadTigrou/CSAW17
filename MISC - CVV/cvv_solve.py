import socket
import re
import random
import time

cards_all = []
for card in open("cards_all", 'r'):
    cards_all.append(card)
cards_mc = []
for card in open("cards_mc", 'r'):
    cards_mc.append(card)
cards_amex = []
for card in open("cards_amex", 'r'):
    cards_amex.append(card)
cards_discover = []
for card in open("cards_discover", 'r'):
    cards_discover.append(card)
cards_visa = []
for card in open("cards_visa", 'r'):
    cards_visa.append(card)

def luhncheck(values):
    values_check = []
    for i in range (0, 15):
        if i % 2 == 0:
            if values[i] * 2 <10:
                values_check.append(values[i]*2)
            else:
                values_check.append(values[i]*2 - 9)
        else:
            values_check.append(values[i])
    som = 0
    for v in values_check:
        som += v
    return (10 - (som % 10)) % 10

def gencards_start(start):
    values = start
    for i in range (len(start), 15):
        values.append(random.randrange(0, 10))        
    values.append(luhncheck(values))
    return values

def gencards_stop(end):
    values = []
    for i in range (0, 16-len(end)):
        values.append(random.randrange(1, 10))
        
    for i in end:
        values.append(i)
    correct = luhncheck(values)    
    values[3] = (values[3] - (end[-1] - correct)) % 10
    return values        

flag = ""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("misc.chal.csaw.io", 8308))
i=0
while 1:
    data = s.recv(1024)
    data = data.replace("\n","")
    print data
    if "Visa!" in data:
        s.sendall(cards_visa[0])
        cards_visa.pop(0)
        continue
    if "American Express!" in data:
        s.sendall(cards_amex[0])
        cards_amex.pop(0)
        continue
    if "Discover!" in data:
        s.sendall(cards_discover[0])
        cards_discover.pop(0)
        continue
    if "MasterCard!" in data:
        s.sendall(cards_mc[0])
        cards_mc.pop(0)
        continue
    if "starts with" in data:
        num = data[-5:-1]
        rvalues = gencards_start([int(i) for i in num])
        rep = 0
        for i in rvalues:
            rep *= 10
            rep += i
        s.sendall(str(rep)+'\n')        
        continue
    if "ends with" in data:
        if data[-3] == ' ':
            num = data[-2:-1]
        else:
            num = data[-5:-1]
        
        rvalues = gencards_stop([int(i) for i in num])
        rep = 0
        for i in rvalues:
            rep *= 10
            rep += i
        
        s.sendall(str(rep)+'\n')
        continue
    if "is valid" in data:
        nums = data[-44:-28] 
        print nums
        valcheck = luhncheck([int(i) for i in nums[:-1]])
        print "valcheck", valcheck, nums[-1]
        if valcheck == int(nums[-1]):
            print str(1)+'\n'
            s.sendall(str(1)+'\n')
        else:
            print str(0)+'\n'
            s.sendall(str(0)+'\n')
        continue
    break

    data = None


print "Connection closed."
s.close()
