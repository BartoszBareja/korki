inp = open("dwa_silnia.txt").readlines()
for el in inp:
    strong = 1
    for i in range(1, int(el)+1):
        strong *= i
    strong = str(strong)
    print("Jedności:" + strong[len(strong)-1])
    if len(strong) > 1:
        print("Dziesiątki: " + strong[len(strong)-2])
    else:
        print("Dziesiątki: 0")