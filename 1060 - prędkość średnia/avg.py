lines = open("avg-inp.txt").readlines()

out = ""

for i in range(1, int(lines[0])+1):
    line = lines[i].split(" ")
    vel1 = int(line[0])
    vel2 = int(line[1])

    velout = (2*vel1*vel2)/(vel1+vel2)
    out += str(velout) + "\n"
open("avg-out.txt","w").writelines(out)
print("Wyniki są w pliku: avg-out.txt")