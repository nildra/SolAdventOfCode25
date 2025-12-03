def maxPowerBank(filename):
    fread = open(filename, "r")
    res = 0
    for line in fread.readlines():
        line = line.replace("\n", "")
        max = int(line[0])
        index = 0
        for i in range(1, len(line)-1):
            if int(line[i]) > max:
                max = int(line[i])
                index = i
        max2 = int(line[index+1])
        for j in range(index+1, len(line)):
            if int(line[j]) > max2:
                max2 = int(line[j])
        res += max*10+max2
    print(res)

maxPowerBank("./input.txt")
