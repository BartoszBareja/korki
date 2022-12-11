lines = open("calc2.txt").readlines()

tab = []

for i in range(10):
    tab.append(0)


for line in lines:
    curr = line.split(" ")

    if curr[0] == "z":
        tab[int(curr[1])] = int(curr[2])
        continue

    a = tab[int(curr[1])]
    b = tab[int(curr[2])]

    if curr[0] == "+":
        print(a + b)
    elif curr[0] == "-":
        print(a - b)
    elif curr[0] == "*":
        print(a * b)
    elif curr[0] == "/":
        print(a // b)
    elif curr[0] == "%":
        print(a % b)
