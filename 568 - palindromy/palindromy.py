def rev(text):
    rev = ""

    for ii in range(len(text)):
        rev += tmp[len(text) - 1 - ii]

    return rev


lines = open("palindromy_in.txt").readlines()

file = open("palindormy_out.txt", "w")

for i in range(1, int(lines[0]) + 1):
    count = 0
    tmp = lines[i].strip()

    while tmp != rev(tmp):
        tmp = int(tmp) + int(rev(tmp))
        count += 1
        tmp = str(tmp)
    file.write(tmp + " " + str(count) + "\n")

file.close()
print(f"Rozwiązania znajdują się w pliku: {file.name}")