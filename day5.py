def nbFresh(filename):
    fread = open(filename, "r")
    include = False
    ranges = []
    res = 0
    for line in fread.readlines():
        if line == "\n":
            include = True
            continue
        if not include:
            line = line.split("-")
            start = int(line[0])
            end = int(line[1])
            ranges.append((start, end))
        else:
            for t in ranges:
                if int(line) >= t[0] and int(line) <= t[1]:
                    res += 1
                    break
    print(res)

nbFresh("./input.txt")
