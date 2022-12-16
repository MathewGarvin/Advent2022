input_source = "https://raw.githubusercontent.com/MathewGarvin/Advent2022/main/advent2022day1input.txt"
f = urlopen(input_source)

g = f.readlines()

def d(e):
    b = [0] * e
    c = 0
    
    for a in g:

        if a == b"\n":
            b.append(c)
            c = 0
            b.remove(min(b))

        else:
            c += int(a)

    print(sum(b))

d(1)
d(3)
