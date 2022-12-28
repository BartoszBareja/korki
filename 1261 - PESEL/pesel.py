lines = open("pesel_inp.txt").readlines()

file = open("pesel_out.txt","w")

for i in range(1, int(lines[0]) + 1):
    curr = str(lines[i]).strip()
    count = 0
    for ii in range(len(curr)):
        if ii == 0 or ii == 4 or ii == 8 or ii == 10:
            count += int(curr[ii])
        elif ii == 1 or ii == 5 or ii == 9:
            count += int(curr[ii]) * 3
        elif ii == 2 or ii == 6:
            count += int(curr[ii]) * 7
        elif ii == 3 or ii == 7:
            count += int(curr[ii]) * 9

    count = str(count)
    if int(count[len(count) - 1]) == 0:
        file.write("D\n")
    else:
        file.write("N\n")

file.close()
