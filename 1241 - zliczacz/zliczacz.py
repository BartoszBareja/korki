lines = open("zliczacz_inp.txt").readlines()


file = open("zliczacz_out.txt","w")
words = ""

for i in range(1,int(lines[0])+1):
    words += lines[i].strip()

for ii in range(ord("a"), ord("z")+1):
    count = 0
    for i in words:
        if ord(i) == ii:
            count += 1

    if count > 0:
        file.write(chr(ii) + ":" + str(count) + "\n")

for ii in range(ord("A"), ord("Z")+1):
    count = 0
    for i in words:
        if ord(i) == ii:
            count += 1

    if count > 0:
        file.write(chr(ii) + ":" + str(count) + "\n")

file.close()