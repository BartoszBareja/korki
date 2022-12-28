lines = open("wycinanie_in.txt").readlines()

file = open("wycinanie_out.txt","w")

for line in lines:
    tab = line.split(" ")
    tmp = ""
    for i in tab[1]:
        if i != tab[0]:
            tmp += i
    file.write(tmp)

file.close()
