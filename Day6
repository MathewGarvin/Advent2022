from urllib.request import urlopen

input_source = "https://raw.githubusercontent.com/MathewGarvin/Advent2022/main/advent2022day6input.txt"
f = urlopen(input_source)

a = f.read()

def F(n):
    i = n
    b = n * '0'
    
    while sum(b.count(b[c]) for c in range(n)) > n:
        b = a[i-n:i]
        i += 1        
            
    print(i - 1)
    
F(4)
F(14)
