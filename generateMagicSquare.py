#!/usr/bin/env python3

####################################################################################
############################# check_magic_square.py ################################
# Python 3.3
# Version: 1.0
# Author: Nicolas Chen

# Description: This python script generates a magic square for odd size only.
####################################################################################

def generate_magic_square(size):
    if size % 2 != 0:
        magicSquare = [[0 for i in range(size)] for j in range(size)]
        rowSquare = 0;
        columnSquare = size // 2;

    for i in range(1, size * size + 1):
        magicSquare[rowSquare][columnSquare] = i;
        rowSquarePlus = rowSquare + 1;
        columnSquarePlus = columnSquare + 1;
        rowSquare = (rowSquare + size - 1) % size;
        columnSquare = (columnSquare + 1) % size;
        if magicSquare[rowSquare][columnSquare] != 0:
            rowSquare = rowSquarePlus;
            columnSquare = columnSquarePlus - 1;

    for row in magicSquare:
        print(row)
    return magicSquare

	
def check_magic_square(squareMatrix):
    rowSize = len(squareMatrix[0])
    sumList = []

    # Vertical:
    for column in range(rowSize):
        sumList.append(sum(row[column] for row in squareMatrix))

    # Horizontal
    sumList.extend([sum(lines) for lines in squareMatrix])

    # Diagonals
    diagonalLeftResult = 0
    for i in range(0, rowSize):
        diagonalLeftResult += squareMatrix[i][i]
    sumList.append(diagonalLeftResult)

    diagonalRightResult = 0
    for i in range(rowSize - 1, -1, -1):
        diagonalRightResult += squareMatrix[i][i]
    sumList.append(diagonalRightResult)

    if len(set(sumList)) > 1:
        return False
    return True

def main():
    print("Welcome in the generation of the magic square")
    sizeSquare = 0

    while (int(sizeSquare) < 3) or (int(sizeSquare) % 2 == 0):
        sizeSquare = int(input("Type the size of the magic square (at least 3 and odd size): "))

    print('{0} x {1} Magic Square:'.format(sizeSquare, sizeSquare))
   
    isMagicSquare = check_magic_square(generate_magic_square(sizeSquare))

    if isMagicSquare:
        print("\nThe magic square is True")
    else:
        print("\nThe magic square is False")


# run the main function only if this module is executed as the main script
# if you import this as a module then nothing is executed
if __name__ == '__main__':
    main()