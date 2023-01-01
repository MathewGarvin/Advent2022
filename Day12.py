f = urlopen(input_source)
#------------------------

L = len

d = f.read()
F = d.find
s = F(b"S")
e = F(b"E")
d = d.replace(b"S", b"a").replace(b"E", b"z").split()
h = L(d)
b = L(d[0])
s = (s % (1 + b), s // (1 + b))
e = (e % (1 + b), e // (1 + b))


D = lambda i, j, m, p, q: [(i + p, j + q)] * (0 if i * p + j * q > b * (p > 0) + h * (q > 0) - (p + q > 0) - 1 
                                              else m > d[j + q][i + p] - 2)

def P(a):
    i = a % b
    j = a // b
    m = d[j][i]

    return (i, j), (m, 
                    [(i, j)] 
                    + D(i, j, m, 0, -1) 
                    + D(i, j, m, 1, 0) 
                    + D(i, j, m, 0, 1) 
                    + D(i, j, m, -1, 0))


k = {P(a)[0]: P(a)[1] for a in range(h * b)}


def F(s):
    x = 0
    q = 0

    h = [{s}]

    while not (x or q):
        i = L(h) - 1
        p = []

        for r in h[i]:
            p += k[r][1]
            
        h += [set(p)]
        x = e in p
        q = h[i + 1] == h[i]
        
    return L(h) - 1 if x else 0

u = [F(i) for i in k if k[i][0] == 97]

print(F(s), min([a for a in u if a]))

#------------------------
f.close()
