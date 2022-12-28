lines = open('polowa_inp.txt').readlines()

file = open("polowa_out.txt", "w")

for i in range(1, int(lines[0]) + 1):
    curr = lines[i]

    tmp = ""
    for i in range(len(curr) // 2):
        tmp += curr[i]
    file.write(tmp + "\n")
