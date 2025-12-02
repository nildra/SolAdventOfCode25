def findInvalid(filename):
    fread = open(filename, "r")
    line = fread.readline()
    allRanges = line.split(",")
    sumInvalid = 0
    for rangeID in allRanges:
        ids = rangeID.split("-")
        idStart, idEnd = ids[0], ids[1]
        for currID in range(int(idStart), int(idEnd)+1):
            currID = str(currID)
            if (len(currID) > 1) and (len(currID)%2 == 0):
                left = currID[:len(currID)//2]
                right = currID[len(currID)//2:]
                if left == right:
                    sumInvalid += int(currID)
    print(sumInvalid)
    
# findInvalid("./input.txt")

def findInvalidPart2(filename):
    fread = open(filename, "r")
    line = fread.readline()
    allRanges = line.split(",")
    sumInvalid = 0
    for rangeID in allRanges:
        ids = rangeID.split("-")
        idStart, idEnd = ids[0], ids[1]
        for currID in range(int(idStart), int(idEnd)+1):
            currID = str(currID)
            if (len(currID) > 1):
                if currID in (currID+currID)[1:-1]:
                    sumInvalid += int(currID)
    print(sumInvalid)

findInvalidPart2("./input.txt")
