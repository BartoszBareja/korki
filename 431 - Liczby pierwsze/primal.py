file = open("primal.txt")
inp = file.readlines()
for i in inp:
    for ii in range(1, int(i)+1):
        if int(i) == ii:
            print("TAK")
            break
        if int(i) % ii == 0:
            print("NIE")
            break
