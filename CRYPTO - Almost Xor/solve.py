# 

def to_num(s):
    x = 0
    for i in range(len(s)): x += ord(s[-1-i]) * pow(256, i)
    return x

def get_nums(s, n):
    sections = [s[i:i+n] for i in range(0, len(s), n)]
    sections[-1] = sections[-1] + ("\x00" * (n - len(sections[-1])))
    return [to_num(x) for x in sections]

def get_vals(x, n):
    vals = []
    mask = (1 << n) - 1
    #print x, n, mask,
    for i in range(8):
        vals.append(x & mask)
        x = x >> n
    #print vals
    vals.reverse()
    return vals

def get_chrs(val_list, n):
    x = val_list[0]
    chrs = []
    for i in range(1, len(val_list)):
        x <<= n
        x += val_list[i]
    for i in range(n):
        chrs.append(chr(x % 256))
        x //= 256
    chrs.reverse()
    return "".join(chrs)

def encr_vals(m_chr, k_chr, n):
    #print m_chr, m_chr, ((m_chr + k_chr) & ((1 << n) - 1))
    return (m_chr + k_chr) & ((1 << n) - 1)

def encrypt(k, m, n):
	if (n >= 8): raise ValueError("n is too high!")
	rep_k = k * (len(m) // len(k)) + k[:len(m) % len(k)] # repeated key
	m_val_list = [get_vals(x, n) for x in get_nums(m, n)]
	k_val_list = [get_vals(x, n) for x in get_nums(rep_k, n)]
	#print m_val_list
	#print k_val_list
	m_vals, k_vals, c_vals = [], [], []
	for lst in m_val_list: m_vals += lst
	for lst in k_val_list: k_vals += lst
	c_vals = [encr_vals(m_vals[i], k_vals[i % len(k_vals)], n) for i in range(0, len(m_vals))]
	c_val_list = [c_vals[i:i+8] for i in range(0, len(c_vals), 8)]
	#print m_vals
	#print k_vals
	#print c_vals
	return "".join([get_chrs(lst, n) for lst in c_val_list])

def decr_vals(m_chr, k_chr, n):
    #print m_chr, m_chr, ((m_chr + k_chr) & ((1 << n) - 1))
    return (m_chr - k_chr) & ((1 << n) - 1)

def decrypt(k, m, n):
    if (n >= 8): raise ValueError("n is too high!")
    rep_k = k * (len(m) // len(k)) + k[:len(m) % len(k)] # repeated key
    m_val_list = [get_vals(x, n) for x in get_nums(m, n)]
    k_val_list = [get_vals(x, n) for x in get_nums(rep_k, n)]
    #print m_val_list
    #print k_val_list
    m_vals, k_vals, c_vals = [], [], []
    for lst in m_val_list: m_vals += lst
    for lst in k_val_list: k_vals += lst
    c_vals = [decr_vals(m_vals[i], k_vals[i % len(k_vals)], n) for i in range(0, len(m_vals))]
    c_val_list = [c_vals[i:i+8] for i in range(0, len(c_vals), 8)]
    #print m_vals
    #print k_vals
    #print c_vals
    return "".join([get_chrs(lst, n) for lst in c_val_list])

ciphertext = '\x80\x9f\xdd\x88\xda\xfa\x96\xe3\xee\x60\xc8\xf1\x79\xf2\xd8\x89\x90\xef\x4f\xe3\xe2\x52\xcc\xf4\x62\xde\xae\x51\x87\x26\x73\xdc\xd3\x4c\xc9\xf5\x53\x80\xcb\x86\x95\x1b\x8b\xe3\xd8\x42\x98\x39'
flag = "flag{"
n = 3
nb_ok = (((8*len(flag))//f)*f)//8
keypart = decrypt(flag,ciphertext, f)[:nb_ok]
print keypart.encode('hex')
print len(ciphertext)
print f, nb_ok
keypart = '\x3e\xb3\xbc\x25\xe1'

for i in range(192, 256):
    key = keypart+chr(i)
    print i, decrypt(key, ciphertext, n)
    
# Solution :
key = '\x3e\xb3\xbc\x25\xe1\xc4'
print decrypt(key, ciphertext, n)



