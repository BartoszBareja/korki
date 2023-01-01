file = open("nwd_out.txt", "w")


def nwd(a, b):
    curr = 0

    if a == b:
        print(a)
    else:
        while a != b:
            if a > b:
                while a > b:
                    a -= b
            elif b > a:
                while b > a:
                    b -= a
        file.write(str(a) + "\n")


lines = open("nwd_in.txt").readlines()

for i in range(1, int(lines[0]) + 1):
    tab = lines[i].split(" ")
    nwd(int(tab[0]), int(tab[1]))

file.close()

print("Odpowiedzi znajdują się w pliku: " + file.name)
