f = urlopen(input_source)
#------------------------

E = enumerate
T = type
L = len
S = sum

G = lambda x: x / abs(x) if x else 0

l = f.read().split(b"\n\n")
l = [a.split() for a in l]


def D(s):
        
    if s[0] == 91:
        c = [0]
        d = 0
        v = []
        
        for i, a in E(s[1:-1], 1):
            
            if a in [91, 93]:
                d += 92 - a
                
            if a == 44:
                
                if d < 1:
                    c += [i]
            
        c += [(L(s) - 1)]
        
        for p, q in zip(c[0:-1], c[1:]):
            
            if p + 2 > q:
                v += []
                
            else:
                v += [(D(s[p + 1 : q]))]
            
    else:
        v = int(s)
    
    return v


l = [[D(a) for a in b] for b in l]
x = [i for p in l for i in p]


def P(l, r):
    
    def C():
        i = 0
        v = 0
        
        while i < min(L(l), L(r)) and v == 0:
            v = P(l[i], r[i])
            i += 1
            
        if v == 0:
            v = G(L(r) - L(l))
            
        return v
    
    if T(l) == list:
        
        if T(r) == int:
            r = [r]
            
        v = C()
        
    elif T(r) == list:
        l = [l]
        v = C()
            
    else:
        v = G(r - l)
        
    return v


K = lambda k: S([P(i, [[2 * k]]) for i in x]) + k + 1 + L(x)

print(S([i * (c > 0) for i, c in E([P(i[0], i[1]) for i in l], 1)]), K(1) * K(3) / 4)

#------------------------
f.close()
