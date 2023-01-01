def decToOther(liczba, system):
    tab = []

    while liczba > 0:

        if liczba // system != liczba / system:
            tab.append(liczba % system)
        else:
            tab.append(0)
        liczba = liczba // system

    out = ""

    for i in range(len(tab)):
        out += str(tab[len(tab) - 1 - i])

    return out


print("Wpisz liczbę do konwersji")
liczba = int(input())

print("Wpisz system do konwersji")
system = int(input())

print(decToOther(liczba, system))


def otherToDec(liczba, system):
    systemOrg = system
    count = 0
    liczba = str(liczba)

    tab = []

    for i in range(len(liczba)):
        tab.append(liczba[len(liczba) - 1 - i])

    if liczba[len(liczba) - 1] != 0:
        count += int(liczba[0])

    tab[0] = "0"

    for i in range(1, len(tab)):
        count += int(tab[i]) * system
        system *= systemOrg

    return count


print("Wpisz liczbę do konwersji")
liczba = int(input())

print("Wpisz system z którego chcesz przekonwertować konwersji")
system = int(input())

print(otherToDec(liczba, system))
