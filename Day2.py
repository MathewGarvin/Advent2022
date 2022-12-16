from urllib.request import urlopen
input_source = "https://raw.githubusercontent.com/MathewGarvin/Advent2022/main/advent2022day2input.txt"
f = urlopen(input_source)

i = f.read()

r = [[8, 3, 4], [5, 9, 1], [2, 6, 7]]
s = 0
t = 0

for b, c in zip(i[::4], i[2::4]):
    b -= 65
    c -= 89
    s += r[b][c]
    t += r[b][b + c - 1]

print(s, t)
