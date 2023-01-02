# funkcja, która zamieni dowolną liczbę na dowolny napis
def zamiana(liczba):
    tab = []

    curr = 10
    curr2 = 10

    count = 0

    out = ""
    while curr < liczba:
        curr *= 10
        curr2 *= 10
        count += 1

    curr2 = curr2 // 10
    sub = .1 * curr
    while curr > liczba:
        curr -= sub

    tab.append(curr / curr2)

    while count != 0:

        liczba = liczba - curr
        curr = curr2

        sub = .1 * curr
        curr2 = curr2 // 10
        while curr > liczba:
            curr -= sub

        tab.append(curr // curr2)
        count -= 1

    for i in tab:
        out += chr(48 + int(i))

    return out


# funkcja odwrotna do powyższej

def re_zamiana(liczba):
    count = 0

    length = len(liczba)

    mult = 1

    for i in range(length):
        mult *= 10

    for i in range(length):
        count += (ord(liczba[i]) - 48) * mult
        mult = mult//10

    return count//10


liczba = int(input())
print(zamiana(liczba))

liczba = input()
print(re_zamiana(liczba))
