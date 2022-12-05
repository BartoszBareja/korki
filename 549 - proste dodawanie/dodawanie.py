test_num = input("Podaj liczbę testów ")
for i in range(int(test_num)):
    tab_out = []
    n = input("Podaj liczbę n w teście ")
    tmp = input("Podaj liczby do dodania ")
    tab = tmp.split(" ")
    out = 0
    for i in tab:
        out += int(i)
    tab_out.append(out)
    print(out)