lines = open("stack.txt").readlines()

tab = []

for i in range(10):
    tab.append(0)

idx = 0

for i in range(len(lines)):
    lines[i] = lines[i].strip()
    if lines[i] == "+":
        if idx > 9:
            print(":(")
            continue
        tab[idx] = lines[i + 1]
        idx += 1
        i += 1
        print(":)")
        continue
    elif lines[i] == "-":
        idx -= 1
        if idx < 0:
            print(":(")
            continue
        print(tab[idx])
        tab[idx] = 0