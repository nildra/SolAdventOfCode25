def rollAdjacent(filename):
    fread = open(filename,"r")
    matrix = [[0 for _ in range(0, 141)]]
    res = 0
    for line in fread.readlines():
        tabLine = [0]
        for charac in line:
            if charac == "@":
                tabLine.append(1)
            elif charac == ".":
                tabLine.append(0)
        tabLine.append(0)
        matrix.append(tabLine)
    matrix.append([0 for _ in range(0, 141)])

    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[i])-1):
            if matrix[i][j] == 0:
                continue
            sumNeighbor = 0
            sumNeighbor += matrix[i-1][j-1] + matrix[i-1][j] + matrix[i-1][j+1] + \
                           matrix[i][j-1] + matrix[i][j+1] + \
                           matrix[i+1][j-1] + matrix[i+1][j] + matrix[i+1][j+1]

            if sumNeighbor < 4:
                res += 1
    print(res)

rollAdjacent("./input.txt")
