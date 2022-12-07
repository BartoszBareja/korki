lines = open("suma.txt").readlines()

curr = 0

for line in lines:
    curr += int(line)
    print(curr)