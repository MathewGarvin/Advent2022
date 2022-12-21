from urllib.request import urlopen
input_source = "https://raw.githubusercontent.com/MathewGarvin/Advent2022/main/advent2022day7input.txt"
f = urlopen(input_source)

t = {}
k = b"/"
b = k.join

for a in f.readlines():
    r = a.split()
    
    if a[0] == 36:
        
        if r[1] == b"cd":
            s = r[2]
            
            if s == k:
                p = [k]
            
            elif s == b"..":
                p.pop()
            
            else:
                p.append(s)
                
        else:
            t[b(p)] = 0
    
    elif a[0] != 100:
        
        for n in range(len(p)):
            t[b(p[ : n+1])] += int(r[0])
            
print(sum(t[a] for a in t if t[a] <= 1e5), min([t[a] for a in t if t[a] >= t[k] - 4e7]))

f.close()
