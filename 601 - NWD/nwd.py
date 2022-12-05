file = open("nwd.txt").readlines()
for i in range(1, int(file[0]) + 1):
    tmp = file[i].split(" ")
    curr = 0
    if int(tmp[0]) > int(tmp[1]):
        curr = int(tmp[0])
    elif int(tmp[0]) < int(tmp[1]):
        curr = int(tmp[1])
    else:
        print(tmp[0])
        break

    for i in range(curr):
        curr -= 1
        if int(tmp[0]) % curr == 0 and int(tmp[1]) % curr == 0:
            print(curr)
            break

        if curr == 1:
            print(1)
            break
