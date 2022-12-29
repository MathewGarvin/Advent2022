from urllib.request import urlopen
input_source = "https://raw.githubusercontent.com/MathewGarvin/Advent2022/main/advent2022day10input.txt"
f = urlopen(input_source)
#------------------------

x = [1]

for l in f.readlines():
    i = len(x)
    x += [x[i - 1]]
    
    if l[0] < 98:
        x += [x[i] + int(l[5:])]
        
c = 0
t = ""

for s in x:
    a = -2 < c - s < 2
    t += "\n" * (c < 1) + "#" * a + "." * (1 - a)
    c += 1
    c %= 40
    
print(sum([(a + 1) * x[a] for a in range(19, 259, 40)]), t)

#------------------------
f.close()
