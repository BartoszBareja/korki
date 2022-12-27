#(x+ y -zy)/(z-1)
lines = open("ciaz_inp.txt").readlines()
tab = []

file = open("ciaz_out.txt", "w")
for i in range(1,int(lines[0])+1):
    curr = lines[i].split(" ")
    out = (int(curr[0]) + int(curr[1]) - (int(curr[1]) * int(curr[2])))/(int(curr[2]) - 1)
    file.write(str(round(out*-12)) + "\n")

file.close()