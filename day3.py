class DayThree():

  paths = [[[3,1]],[[1,1],[3,1],[5,1],[7,1],[1,2]]]

  def pathCalc(self, mapFile, partNum):
    result = 1
    stepList = self.paths[partNum - 1]
    treesList = []
    while len(mapFile[0]) < len(mapFile)*7:
      for i in range(len(mapFile)):
        mapFile[i] += mapFile[i]
    for x in range(len(stepList)):
      stepX = stepList[x][0]
      stepY = stepList[x][1]
      posX = 0
      totTrees = 0
      for i in range(0, len(mapFile), stepY):
        if mapFile[i][posX] == "#":
          totTrees += 1
        posX += stepX
      treesList.append(totTrees)
    for y in range(len(treesList)):
      result *= treesList[y]
    # return "Rows: " + str(len(mapFile)) + " Cols: " + str(len(mapFile[0]))
    return result

