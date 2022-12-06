from urllib.request import urlopen
s = "https://raw.githubusercontent.com/MathewGarvin/Advent2022/main/advent2022day5input.txt"

def F(p):
    f = urlopen(s)
    a = s
    t = []

    while a[1] != '1':
        a = f.readline().decode()
        t.append(a[1::4])

    t = [''.join(s).strip() for s in zip(*t)]
    
    for d in '12':
        a = f.readline()

    while a != b'':
        b = [int(d) for d in a.split()[1::2]]
        c = b[1] - 1
        e = b[2] - 1
        t[e] = (1 - p) * t[c][b[0]-1::-1] + p * t[c][0:b[0]] + t[e]
        t[c] = t[c][b[0]:]
        a = f.readline()

    print(''.join([d[0] for d in t]))

F(0)
F(1)
