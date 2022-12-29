from urllib.request import urlopen
input_source = "https://raw.githubusercontent.com/MathewGarvin/Advent2022/main/advent2022day8input.txt"

f = urlopen(input_source)

j = f.read().split()

r = range
l = len
t = sum

g = l(j[0])
h = l(j)
z = []
o = g * h
g -= 1
h -= 1

v = lambda k: l(k) - max(k) + (sum(k) > 0)

def m(a, b, x, y):
    c = g * (a < 0)
    d = h * (b < 0)    
    return [(i + 1) * (j[x][y] <= j[x * b * b + c + i * a][y * a * a + d + i * b]) 
            for i in r(x * a + y * b + c + d)]

for y in r(1, h):
    
    for x in r(1, g):
        n = m(1, 0, x, y)
        e = m(0, -1, x, y)
        s = m(-1, 0, x, y)
        w = m(0, 1, x, y)
        
        z += [v(n) * v(e) * v(s) * v(w)]
        o -= t(n) * t(e) * t(s) * t(w) > 0
        
print(o, max(z))

f.close()
