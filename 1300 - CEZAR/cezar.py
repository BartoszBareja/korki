lines = open("cezar_inp.txt").readlines()

file = open("cezar_out.txt","w")

for i in lines:
    out = ""
    for ii in i:
        curr = ord(ii)
        if 87 >= curr >= 65:
            curr = curr+3
        elif curr > 87:
            curr = ord("A") + (ord("Z") - (curr+3))
        out += chr(curr)
    file.write(out)
