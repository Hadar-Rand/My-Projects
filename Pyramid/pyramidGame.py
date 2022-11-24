import random

pyramid =[[],[],[],[],[]]    #matrix with 5 rows
colors = ['Blue', 'Pink', 'Yellow']
pyramidCorrectGlobal1 = False       #to know if the pyramid is Correct (change each time there is a problem noBlueOnEdges)
pyramidCorrectGlobal2 = False       #to know if the pyramid is Correct (change each time there is a problem noPinkNextToBlue)
pyramidCorrectGlobal3 = False       #to know if the pyramid is Correct (change each time there is a problem in noFourYellows)
startIndex = 4
endIndex = 5
lenOfRow = 9
numOfLines = 5


"""
Rules:
Blue can not be on edge of pyramid        (and at row 0, or 4 as well)
Pink can not be on the sides of blue        (up(if not in row zero), down(if not in row 4), sides(if not in column 0 or 8))
Yellow can not appear more then 4 time in one row  
"""

#fills Pyramid
def fillPyramid():
    startIndex = 4                                                            #indexs to start putting random numbers in pyramid (for range in for loop)
    endIndex = 5                                                              #index to stop putting random numbers in pyramid (for range in for loop)

    #filling the matrix with zeros
    for row in pyramid:
        for column in range(lenOfRow):
            row.append(0)

    #creating a pyramid of random numbers inside of the matrix
    for row in pyramid:
        for column in range(startIndex, endIndex):
            row[column] = random.choice(colors)                                  #add the correct number of random numbers in row
        startIndex -= 1
        endIndex += 1


#checks that there are no blue spots at edges of pyramid
def noBlueOnEdges(pyramidCorrect, change):
    pyramidCorrect = True
    startIndex = 4
    endIndex = 5

    #if theres blue on the top row of the pyramid
    if pyramid[0][startIndex] == 'Blue':
        if change:
            pyramid[0][startIndex] = random.choice(colors)
        pyramidCorrect = False


    #if theres blue on the bottom row of the pyramid
    for column in range(0,lenOfRow):
        if pyramid[4][column] == 'Blue':
            if change:
                pyramid[4][column] = random.choice(colors)
            pyramidCorrect = False

    startIndex = 3
    endIndex = 5
    #if there is blue on outline of pyramid changed randomly
    for row in range(1, numOfLines - 1):
        if pyramid[row][startIndex] == 'Blue':
            if change:
                pyramid[row][startIndex] = random.choice(colors)
            pyramidCorrect = False
        if pyramid[row][endIndex] == 'Blue':
            if change:
                pyramid[row][endIndex] = random.choice(colors)
            pyramidCorrect = False
        startIndex -= 1;
        endIndex += 1;

    return pyramidCorrect                                                #returns if everything was okay with the pyramid and if there where any changes made this iteration




#checks that there are no pink spots next to blue spots
def noPinkNextToBlue(pyramidCorrect, change):
    pinkChanged = False                                                      #if the spot pyramid was already changed it shouldn't be changed again till next iteration
    pyramidCorrect = True
    for row in range (0, numOfLines):
        for column in range(0,lenOfRow):
            if pyramid[row][column] == 'Pink':
                if row != 4:                                                               #as long as row is not bottom row of pyramid check the row under
                    if pyramid[row + 1][column] == 'Blue':
                        if change:
                            pyramid[row][column] = random.choice(colors)
                            pinkChanged = True
                        pyramidCorrect = False
                if column != 0:                                                              #as long as column is not first column of pyramid check the column to the left
                    if pyramid[row][column - 1] == 'Blue' and not pinkChanged:
                        if change:
                            pyramid[row][column] = random.choice(colors)
                            pinkChanged = True
                        pyramidCorrect = False
                if column != 8:                                                              #as long as column is not last column of pyramid check the column to the right
                    if pyramid[row][column + 1] == 'Blue' and not pinkChanged:
                        if change:
                            pyramid[row][column] = random.choice(colors)
                            pinkChanged = True
                        pyramidCorrect = False
                if row != 0:                                                                  #as long as row is not top row of pyramid check the row above
                    if pyramid[row - 1][column] == 'Blue' and not pinkChanged:
                        if change:
                            pyramid[row][column] = random.choice(colors)
                            pinkChanged = True
                        pyramidCorrect = False
                pinkChanged = False
    return pyramidCorrect                                                                     #returns if everything was okay with the pyramid and if there where any changes made this iteration

#checks that there are not 4 yellows in the same row
def noFourYellows(pyramidCorrect):
    pyramidCorrect = True
    startIndex = 4                                                                           #indexs to start putting random numbers in pyramid (for range in for loop)
    endIndex = 5
    for row in range(0, numOfLines):
        counter = 0
        #counts number of yellows in one row
        for column in range(0, lenOfRow):
            if pyramid[row][column] == 'Yellow':
                counter += 1
        #if there are more then 4 yellows randomizes a new row keeping the form of the pyramid
        if counter > 4:
            for column in range(startIndex, endIndex):
                pyramid[row][column] = random.choice(colors)
                pyramidCorrect = False
        startIndex -= 1
        endIndex += 1

    return pyramidCorrect                                               #returns if everything was okay with the pyramid and if there where any changes made this iteration

def printPyramid():
    #prints pyramid (upside down)
    space = ""
    for row in range(0, numOfLines):
        print(space, pyramid[row])
        space += "     "

#runs the methods to create pyramid by the rules of the game
fillPyramid()

#checks that the pyramid follows all three rules if not changes it with the methods
while not pyramidCorrectGlobal1 or not pyramidCorrectGlobal2 or not pyramidCorrectGlobal3:

    pyramidCorrectGlobal1 = noBlueOnEdges(False, True)
    pyramidCorrectGlobal2 = noPinkNextToBlue(False, True)
    pyramidCorrectGlobal3 = noFourYellows(False)

    # if the pyramid is changed checks that the other conditions are still true (without changing!)
    if pyramidCorrectGlobal2:
        pyramidCorrectGlobal1 = noBlueOnEdges(False, False)

    if pyramidCorrectGlobal3:
        pyramidCorrectGlobal1 = noBlueOnEdges(False, False)
        pyramidCorrectGlobal2 = noPinkNextToBlue(False, False)

#printing the final pyramid
for row in pyramid:
    print(row)

