lines = open("tagi_in.txt").readlines()

file = open("tagi_out.txt", "w")

for line in lines:
    change = False
    tmp = ""
    for i in line:
        if i == ">":
            change = False
            tmp += i
            continue

        if change and ord("a") <= ord(i) <= ord("z"):
            tmp += chr(ord(i) - (ord("z")-ord("Z")))
            continue

        if i == "<":
            change = True
            tmp += i
            continue

        tmp += i
    file.write(tmp)
file.close()
