lines = open("./euklides.txt").readlines()

for i in range(1,int(lines[0])+1):
    curr = lines[i].split(" ")
    a = int(curr[0])
    b = int(curr[1])

    while a != b:
        if a > b:
            a = a-b
        elif b > a:
            b = b - a
    print(a+b)