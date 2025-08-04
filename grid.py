from random import sample
from selection import SelectNumber
from copy import deepcopy

def createLineCoordinates(cellSize: int) -> list[list[tuple]]:
    """creates the x, y coordinates for drawing the grid lines"""
    points = []
    for y in range(1, 9):
        #horizontal lines
        temp = []
        temp.append((0, y*cellSize)) #x, y points [(0, 100), (0, 200), (0, 300), (0,400)...]
        temp.append((cellSize*9, y*cellSize)) #x, y points [(900, 100), (900, 200), (900, 300),..]
        points.append(temp)

    for x in range(1, 10): #1->10 to close the grid from the right side
        #vertical lines
        temp = []
        temp.append((x*cellSize, 0)) #x, y points [(100, 0), (200, 0), (300, 0),(400,0)...]
        temp.append((x*cellSize, cellSize*9)) #x, y points [(100, 900), (900,200),(900, 300),...]
        points.append(temp)
    return points

subGridSize = 3
gridSize = subGridSize * subGridSize

def pattern(rowNum: int, colNum:int) -> int:
    return (subGridSize * (rowNum % subGridSize) + rowNum // subGridSize + colNum) % gridSize

def shuffle(samp: range) -> list:
    return sample(samp, len(samp))

def createGrid(subGrid:int) -> list[list]:
    #creates the 9x9 grid filled with random numbers
    rowBase = range(subGrid)
    rows = [g * subGrid + row for g in shuffle(rowBase) for row in shuffle(rowBase)]
    columns = [g * subGrid + column for g in shuffle(rowBase) for column in shuffle(rowBase)]
    nums = shuffle(range(1, subGrid * subGrid + 1))
    return [[nums[pattern(row, column)] for column in columns] for row in rows]

def removeNumbers(grid:list[list]) -> None:
    #randomly sets numbers to zeros on the grid
    numOfCells = gridSize * gridSize
    empties = numOfCells * 3 // 9 #7 is ideal -- higher than this num == easier game
    for i in sample(range(numOfCells), empties):
        grid[i // gridSize][i % gridSize] = 0


class Grid:
    def __init__(self, pygame, font):
        self.cellSize = 90
        self.numXoffset = 30
        self.numYoffset = 10
        self.lineCoordinates = createLineCoordinates(self.cellSize)
        self.win = False
        self.grid = createGrid(subGridSize)
        self.__test_grid = deepcopy(self.grid)
        removeNumbers(self.grid)

        self.occupiedcellCoordinates = self.preoccupiedCells()
        # print(self.occupiedcellCoordinates) #this allows us to see the coordinates of the cells

        self.gameFont = font

        self.numberCounts = {i: 0 for i in range(1,10)} #counts both correct and mistaken numbers
        self.correctCounts = {i: 0 for i in range(1,10)}
        
        self.selection = SelectNumber(pygame, self.gameFont)
        self.selection.setGridReference(self)

        self.updateNumberCounts = self.updateNumCounts()

    def updateNumCounts(self) -> None:
        self.numberCounts = {i: 0 for i in range(1,10)}
        self.correctCounts = {i: 0 for i in range(1,10)}
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                num =  self.grid[y][x]
                if num != 0:
                    self.numberCounts[num] += 1

                    if num == self.__test_grid[y][x]:
                        self.correctCounts[num] += 1

    def restart(self) -> None:
        self.grid = createGrid(subGridSize)
        self.__test_grid = deepcopy(self.grid)
        removeNumbers(self.grid)
        self.occupiedcellCoordinates = self.preoccupiedCells()
        self.win = False

    def checkGrids(self):
        #if every cell in the actual grid equals every cell in the test grid, then it return true
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] != self.__test_grid[y][x]:
                    return False
        return True        

    def isCellPreoccupied(self, x:int, y:int) -> bool:
        #check for non playable cells - preoccupied/initialized cells
        for cell in self.occupiedcellCoordinates:
            if x == cell[1] and y == cell[0]: # x= column, y= row
                return True
        return False

    def getMouseClick(self, x:int, y:int) -> None:
        if x <= (self.cellSize*9): #810 pixels
            gridX, gridY = x // self.cellSize, y // self.cellSize 
            # print(gridX, gridY)
            if not self.isCellPreoccupied(gridX, gridY):
                self.setCell(gridX, gridY, self.selection.selectedNum)
                self.updateNumCounts()
        self.selection.btnClicked(x, y)
        if self.checkGrids():
            # print("Won, Game Over!")
            self.win = True

    def preoccupiedCells(self)-> list[tuple]:
        #gather the y,x coordinates for all preoccupied/initalized cells
        occupiedCellCoordinates = []
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.getCell(x, y) != 0:
                    occupiedCellCoordinates.append((y, x)) # first the row, then the column: y, x
        return occupiedCellCoordinates

    def __drawNumbers(self, surface) ->  None: #the two underrscores indicate that the function is private
        #draw the grid numbers
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.getCell(x,y) != 0:
                    if (y, x) in self.occupiedcellCoordinates:
                        textSurface = self.gameFont.render(str(self.getCell(x,y)), False, (99,52,71)) #draw numbers in their default color
                    else:
                        textSurface = self.gameFont.render(str(self.getCell(x,y)), False, (0,255,0)) #draw numbers in green
                    
                    if self.getCell(x, y) != self.__test_grid[y][x]:
                        textSurface = self.gameFont.render(str(self.getCell(x,y)), False, (255,0,0)) #draw numbers in red

                    surface.blit(textSurface, 
                                 (x * self.cellSize + self.numXoffset, 
                                  y *self.cellSize + self.numYoffset))

    def getCell(self, x:int, y:int) -> int:
        #get a cell value at y, x coordinate
        return self.grid[y][x]
    
    def setCell(self, x: int, y:int, value: int) -> None:
        #set a cell value at y,x coordinate

        #first decrement count of oldValue if its being replaced
        oldValue = self.getCell(x,y)
        if oldValue != 0:
            self.numberCounts[oldValue] -= 1
            if oldValue == self.__test_grid[y][x]:
                self.correctCounts[oldValue] += 1

        #set new value
        self.grid[y][x] = value

        #increment count of new value if it's not zero
        if value != 0:
            self.numberCounts[value] += 1
            if value == self.__test_grid[y][x]:
                self.correctCounts[value] += 1

    def __drawLines(self, pg, surface) -> None: 
        for index, point in enumerate(self.lineCoordinates):
            pg.draw.line(surface, (0,50,0), point[0], point[1])
            if(index == 2 or index == 5 or index == 10 or index ==13):
                pg.draw.line(surface, (50, 0, 47), point[0], point[1]) #yellow grid lines
            else:
                pg.draw.line(surface, (50, 97, 47), point[0], point[1]) #light black grid lines

    def draw(self, pg, surface):
        self.__drawLines(pg, surface)
        self.__drawNumbers(surface)
        self.selection.draw(pg, surface)
