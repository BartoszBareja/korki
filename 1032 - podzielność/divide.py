lines = open("divide.txt").readlines()

for i in range(1, int(lines[0]) + 1):
    tmp = lines[i].split(" ")
    out = []
    max = int(tmp[0])
    div = int(tmp[1])
    ndiv = int(tmp[2])
    for ii in range(1, max + 1):
        if ii % div == 0 and ii % ndiv != 0:
            out.append(ii)
    print(out)
