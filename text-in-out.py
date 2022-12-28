napis = input()

napis_re = ""

for i in range(len(napis)):
    napis_re += napis[len(napis)-1-i]

print(napis_re)