lines = open("rol.txt").readlines()

for line in lines:
    curr = line.split(" ")
    tab = []

    for i in range(1, int(curr[0]) + 1):
        tab.append(curr[i])

    curr = tab[len(tab) - 1]
    first = tab[0]
    for i in range(1, len(tab)+1):
        tmp = tab[len(tab) - i]
        tab[len(tab) - i] = curr
        curr = tmp
    tab[len(tab)-1] = first
    print(tab)