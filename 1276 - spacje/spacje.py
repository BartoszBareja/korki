lines = open("spacje_in.txt").readlines()

file = open("spacje_out.txt", "w")

for line in lines:
    tmp = ""
    curr = False
    for i in line:

        if curr:
            curr = False
            i = chr(ord(i) - (ord("a") - ord("A")))

        if i != " ":
            tmp += i
        else:
            curr = True

    file.write(tmp)
    print(tmp)

file.close()
