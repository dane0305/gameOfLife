import time
import sys
import random
import json

def startGame(pattern, rows, cols, configurations):
    actualGeneration = 1
    while(1):
        generations = int(input("How many generations would you like to simulate: "))
        if(generations > 0 or generations < 10000):
            break
        print("Invalid number (0 - 10000)")
    grid = initializeGrid(pattern, configurations, rows, cols)
    print("Initial state:")
    printGrid(grid)
    time.sleep(2)
    continueGame(grid, actualGeneration, generations)

def initializeGrid(pattern, configurations, rows, cols):
    grid = list()
    if(pattern == "random"):
        for row in range(rows):
            grid.append(list())
            for col in range(cols):
                if(random.randint(0,1) == 0):
                    char = "."
                else:
                    char = "#"
                grid[row].append(char)
    elif(configurations["patterns"].get(pattern, 0) != 0):
        patternGrid = configurations["patterns"][pattern]
        for row in patternGrid:
            for i in range(cols-len(row)):
                row.append('.')
        newRow = ['.']*cols
        for i in range(rows - len(patternGrid)):
            patternGrid.append(newRow)
        grid = patternGrid
    else:
        raise ValueError("Pattern not found in configuration file")
    return grid

def nextGeneration(grid):
    newGrid = list()
    change = False
    for row in range(len(grid)):
        newGrid.append(list())
        for col in range(len(grid[row])):
            liveN = 0
            if(col < len(grid[row])-1):
                if(grid[row][col+1] == "#"): liveN += 1
                if(row < len(grid)-1):
                    if(grid[row+1][col+1] == "#"): liveN += 1
            if(row < len(grid)-1):            
                if(grid[row+1][col] == "#"): liveN += 1
                if(col > 0):
                    if(grid[row+1][col-1] == "#"): liveN += 1
            if(row > 0):
                if(col > 0):
                    if(grid[row-1][col-1] == "#"): liveN += 1
                if(grid[row-1][col] == "#"): liveN += 1
                if(col < len(grid[row])-1):
                    if(grid[row-1][col+1] == "#"): liveN += 1
            if(col > 0):
                if(grid[row][col-1] == "#"): liveN += 1
            if(liveN == 3 and grid[row][col] == "."):
                change = True
                newGrid[row].append("#")
            elif(grid[row][col] == "#"):
                if(liveN < 2):
                    newGrid[row].append('.')
                    change = True
                elif(liveN > 3):
                    newGrid[row].append('.')
                    change = True
                else:
                    newGrid[row].append(grid[row][col])
            else:
                newGrid[row].append(grid[row][col])

    return newGrid, change
                
def continueGame(grid, generation, maxGeneration):
    while(1):
        grid, change = nextGeneration(grid)
        if(not change):
            print("Final state achieved in generation", generation)
            break
        if(generation == maxGeneration+1):
            print("All generations simulated")
            break
        time.sleep(0.3)
        print("Generation:", generation)
        printGrid(grid)
        generation += 1
    return generation

def printGrid(grid):
    for i in grid:
        string = ""
        for e in i:
            string+=e + " "
        print(string)

def runGame():
    print("\n\n------------")
    print("Game of life")
    print("------------")
    f = open("configuration.json")
    configurations = json.load(f)
    f.close() 
    configurations["patterns"]["random"] = "random"
    print("""\nThe game will start with default options ({} rows, {} columns and random seed)
             \nIf you want to change the options type 0, otherwise type 1 to start the game""".format(configurations["default_rows"], configurations["default_cols"]))
    while(True):
        option = input("Option:")
        if(option == "1" or option == "0"):
            break
        print("Invalid option, try again!")
    if(option == "0"):
        print("Let's change the configurations...")
        while(1):
            rows = int(input("How many rows would you like your world to have (7 - 39): ")) 
            if(rows < 7 or rows > 39):
                print("invalid number of rows, try again!")
            else:
                break
        while(1):
            cols = int(input("How many columns would you like your world to have (12 - 68): "))
            if(cols < 12 or cols > 68):
                print("Invalid number of columns, try again!")
            else:
                break
        configurations["default_rows"] = rows
        configurations["default_cols"] = cols
        print("The possible patterns to choose from are:")
        for pattern in configurations["patterns"]:
            print(pattern, end = "   ")
        print("")
        while(1):
            pattern = input("Write the pattern you would like to start with: ")
            if(configurations["patterns"].get(pattern, 0) != 0):
                break
            print("Pattern not valid, try again!")
    elif(option == "1"):
        pattern = "random"
    startGame(pattern, configurations["default_rows"], configurations["default_cols"], configurations)
if __name__ == '__main__':    
    runGame()