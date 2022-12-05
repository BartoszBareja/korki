inp = open("potegi,txt").readlines()
for i in range(1, len(inp[0]) + 1):
    tmp = inp[i].split(" ")
    curr = 1
    for ii in range(int(tmp[1])):
        curr *= int(tmp[0])
    print(curr)