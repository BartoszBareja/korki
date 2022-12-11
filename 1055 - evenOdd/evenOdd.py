lines = open("evenOdd.txt").readlines()

for i in range(int(lines[0])):
    tab = lines[i+1].split(" ")
    odd = []
    even = []

    for i in range(1,len(tab)):
        if i % 2 == 0:
            even.append(tab[i])
        elif i % 2 != 0:
            odd.append(tab[i])
    print(even, odd)