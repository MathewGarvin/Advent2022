from urllib.request import urlopen
input_source = "https://raw.githubusercontent.com/MathewGarvin/Advent2022/main/advent2022day9input.txt"

f = urlopen(input_source)
#------------------------

r = range

n = [1j]
t = n * 1
c = n * 10

for l in f.readlines():
    
    for p in r(int(l[2:])):
        
        for a in zip([68, 76, 82, 85], [-1j, -1, 1, 1j]):
            c[0] += a[1] * (l[0] == a[0])

        for k in r(9):
            d = c[k] - c[k + 1]
            
            if abs(d) >= 2:
                c[k + 1] += min(1, max(-1, d.real)) + min(1, max(-1, d.imag)) * 1j
        
        n += [c[1]]
        t += [c[9]]
    
print(len(set(n)), len(set(t)))

#------------------------
f.close()
