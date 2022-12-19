from urllib.request import urlopen
input_source = "https://raw.githubusercontent.com/MathewGarvin/Advent2022/main/advent2022day3input.txt"
f = urlopen(input_source)

i = f.readlines()
r = range
s = set
    
def g(n):
    t = 0
    
    for j in r(0, len(i), n):
        d = [s(i[j + m][:-1]) for m in r(n)]
        
        if n < 2:
            l = len(i[j]) // 2
            d = [s(i[j][:l]), s(i[j][l:])]
            
        e = min(s.intersection(*d))
        t += e - 38 - 58 * (e > 90)
        
    print(t)
    
g(1)
g(3)
