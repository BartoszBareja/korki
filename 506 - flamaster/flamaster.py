lines = open("flamaster_inp.txt").readlines()

file = open("flamaster_out.txt", "w")

for i in range(1, int(lines[0]) + 1):
    curr = lines[i]
    out = ""
    count = 1
    for ii in range(0, len(curr)-1):
        if curr[ii] == curr[ii+1]:
            count += 1
        else:
            if count > 2:
                out += curr[ii] + str(count)
                count = 1
            elif count == 2:
                out += curr[ii]
                out += curr[ii]
                count = 1
            else:
                out += curr[ii]
                count = 1
    if count != 1:
        out += curr[len(curr)-1] + str(count)

    file.write(out + "\n")
file.close()
print("Odpowiedzi znajdują się w pliku: " + file.name)