def SearchingChallenge(strArr):
    if strArr is None:
        return "No stuff to solve then"
    matrixNeo = tuple(tuple(int(char) for char in row) for row in strArr)
    column = len(matrixNeo[0])
    row = len(matrixNeo)
    sumOfHole = 0

    def findMe(x, y):
        if x < 0 or x > column or y < 0 or y > row or matrixNeo[x][y] != 0 or accessed[x][y]:
            return
        findMe(x + 1, y)
        findMe(x - 1, y)
        findMe(x, y + 1)
        findMe(x, y - 1)

    accessed = [[False] * column for _ in range(row)]
    for myX in range(column):
        for myY in range(row):
            if matrixNeo[myX][myY] == 0 and accessed[myX][myY] is False:
                accessed[myX][myY] = True
                findMe(myX, myY)
                sumOfHole += 1

    return sumOfHole


# keep this function call here
print(SearchingChallenge(["01111","01101","00011","11110"]))

