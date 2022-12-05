file = open('niekolejne.txt')
inp = file.readlines()
for i in inp:
    if int(i) < 3:
        print("NIE")
    elif int(i) == 3:
        print("2 0 3 1")
    else:
        tab = []
        for ii in range(0, int(i) + 1, 2):
            tab.append(ii)

        for ii in range(1, int(i) + 1, 2):
            tab.append(ii)

        print(tab)