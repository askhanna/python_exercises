def getChessSquareColor(column, row):
    # If the column and row is out of bounds, return a blank string:
    if column > 8 or row > 8 or column < 1 or row < 1:
        return ''

    # If the even/oddness of the column and row match, return 'white':
    if (column + row) % 2 == 0:
        return 'white'

    # If they don't match, then return 'black':
    else:
        return 'black'
    
print(getChessSquareColor(1, 1)) # white
print(getChessSquareColor(1, 2)) # black
print(getChessSquareColor(2, 1)) # black
print(getChessSquareColor(2, 2)) # white
print(getChessSquareColor(8, 8)) # white
print(getChessSquareColor(8, 1)) # black
print(getChessSquareColor(1, 8)) # black
print(getChessSquareColor(9, 2)) # ''
print(getChessSquareColor(0, 9)) # ''   
