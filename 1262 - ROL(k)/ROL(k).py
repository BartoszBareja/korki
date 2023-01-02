lines = open("ROL(k)-inp.txt").readlines()

count = int(lines[0].split(" ")[1])

for i in range(1, len(lines)):
    line = lines[i]
    curr = line.split(" ")
    tab = []

    for i in range(len(curr)):
        tab.append(curr[i])

    for i in range(count):
        curr = tab[len(tab) - 1]
        first = tab[0]
        for i in range(1, len(tab) + 1):
            tmp = tab[len(tab) - i]
            tab[len(tab) - i] = curr
            curr = tmp
        tab[len(tab) - 1] = first

    out = ""
    for item in tab:
        out += item + " "
    open("ROL(k)-out.txt","w").writelines(out)
    print("Wyniki znajdują się w pliku: ROL(k)-out.txt")
