from urllib.request import urlopen
input_source = "https://raw.githubusercontent.com/MathewGarvin/Advent2022/main/advent2022day4input.txt"
f = urlopen(input_source)

i = f.readlines()
y = 0
z = 0

for a in i:
    d, g, h, j = [int(e) for g in a.split(b",") for e in g.split(b"-")]
    y += (h - d) * (j - g) < 1
    z += (d <= j) * (h <= g)

print(y, z)
