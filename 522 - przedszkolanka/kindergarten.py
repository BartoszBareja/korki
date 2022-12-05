file = open("kindergarten.txt").readlines()
for i in range(1, int(file[0]) + 1):
    curr = file[i].split(" ")
    out = int(curr[0])
    for i in range(1, int(curr[1])):
        out += int(curr[0])
        if out % int(curr[1]) == 0:
            break
    print(out)
