lines = open("zliczanie.txt").readlines()
for line in lines:
    count = 0
    tab = line.split(" ")
    searched = tab[0]
    for i in range(2, len(tab)):
        if tab[i] == searched:
            count += 1

    print(count)
