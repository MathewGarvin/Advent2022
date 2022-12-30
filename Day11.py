f = urlopen(input_source)
#------------------------

I = int
R = range

def Q(z, m, x, w):
    o = x == b"old"           
    c = 0 if o else I(x)
    
    if w:
        y = c + o * z
        v = (z * y ** m + y - y * m) // w
        
    else:        
        v = []
        
        for j, d in z:
            y = c + o * j
            v += [(j * y ** m + y - y * m) % d]
        
    return v

    
def B(r, t):
    d = []
    u = b"\n"
    
    for j in h.split(u * 2):
        l = j.split(u)
        d += [[[I(a) for a in l[1][17:].split(b",")], 
             l[2][19:].split()[1:], 
             I(l[3][21:]), 
             I(l[4][29:]), 
             I(l[5][30:]), 
             0]]
        
    v = [m[2] for m in d]
    
    for m in d:
        m += [[[a % w for w in v] for a in m[0]]]

    for _ in R(r):
        n = 0

        for m in d:

            while m[t]:
                m[5] += 1
                p = m[t].pop(0)
                j = Q(zip(p, v) if t else p, m[1][0] == b"*", m[1][1], 3 * (not t))
                g = j[n] < 1 if t else j % m[2] < 1
                    
                d[g * m[3] + (1 - g) * m[4]][t] += [j]
                    
            n += 1

    b = sorted([m[5] for m in d])
    print(b[-2] * b[-1])
    
    
h = f.read()
B(20, 0)
B(10000, 6)

#------------------------
f.close()
