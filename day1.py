def findDoorCode(filename, pos=50):
    count = 0
    fread = open(filename, "r")
    for line in fread.readlines():
        lineTab = list(line)
        number = int("".join(lineTab[1:]))
        if lineTab[0] == "L":
            pos = (pos-number)%100
        elif lineTab[0] == "R":
            pos = (pos+number)%100
        if pos == 0 : 
            count += 1
    print(count)

findDoorCode("./input.txt")
