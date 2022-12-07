lines = open("calc.txt").readlines()

for i in range(len(lines)):
    out = 0
    tab = lines[i].split(" ")
    a = int(tab[1])
    b = int(tab[2])
    if tab[0] == "+":
        out = a + b
    elif tab[0] == "-":
        out = a - b
    elif tab[0] == "*":
        out = a * b
    elif tab[0] == "/":
        out = a // b
    elif tab[0] == "%":
        out = a % b

    print(out)