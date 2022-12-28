napis = input()
napis2 = ""
for i in napis:
    curr = ord(i)
    if ord("a") <= curr <= ord("z"):
        curr = curr - 32
    elif ord("Z") >= curr >= ord("A"):
        curr = curr + 32

    napis2 += chr(curr)
print(napis2)