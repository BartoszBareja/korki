lines = open("avg.txt").readlines()

for i in range(1, int(lines[0])+1):
    tab = lines[i].split(" ")
    avg = 0
    for item in tab:
        avg += int(item)
    avg = avg/len(tab)


    val = int(tab[0])

    for item in tab:
        if abs(avg-int(item)) < abs(avg - val):
            val = int(item)

    print(val)