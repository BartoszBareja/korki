file = open("glutton.txt").readlines()

sec_day = 24 * 60 * 60

for i in range(1, len(file)):
    tmp = file[i].split(" ")
    if len(tmp) == 2:
        tab = []
        boxes = tmp[1]
        for ii in range(int(tmp[0])):
            tab.append(file[i + ii + 1])
        out = 0
        for val in tab:
            out += sec_day // int(val)

        output = out // int(boxes)
        if out % int(boxes) != 0:
            output += 1

        print(output)
