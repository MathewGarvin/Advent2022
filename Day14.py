f = urlopen(input_source)
#------------------------

I = int
R = range
    
def F(p):
    k = []

    for n in [[C(*[I(c) for c in b.split(b",")]) 
               for b in a.split(b" -> ")] for a in s.split(b"\n")]:
        
        for a, z in zip(n[:-1], n[1:]):
            d = z - a

            for n in R(1 + I(abs(d))):
                k += [a + n * d / abs(d)]

    o = 500
    d = I(max([b.imag for b in k])) + 2
    l = I(min(*[b.real for b in k], o - d))
    r = I(max(*[b.real for b in k], o + d)) - l
    o -= l
    
    g = [[1 - (a * p < d)] * (r + 1) for a in R(d + 1)]
    
    for b in k:
        g[I(b.imag)][I(b.real) - l] = 1
        
    m = 2

    while m and g[0][o] == 0:        
        p = 0
        q = o

        while p != q:
            p = q
            r = I(q.real)
            i = I(q.imag)

            if i >= d:
                m = 0
                
            elif g[i + 1][r] < 1:
                q += 1j

            elif g[i + 1][r - 1] < 1:
                q -= 1 - 1j
                
            elif g[i + 1][r + 1] < 1:
                q += 1 + 1j
                
        g[i][r] = m
        
    print(sum(a.count(2) for a in g))

    
s = f.read()[:-1]
F(0)   
F(1)

#------------------------
f.close()
