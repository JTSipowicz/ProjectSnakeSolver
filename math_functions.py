def compareSquares(x1, x2, y1, y2, square1_length, square2_length):
    # Test lower left corner
    if x1 >= x2 and x1 <= (x2 + square2_length) and y1 >= (y2 - square2_length) and y1 <= y2:
        return True 
    # Test upper left corner
    if x1 >= x2 and x1 <= (x2 + square2_length) and (y1 - square1_length) >= (y2 - square2_length) and (y1 - square1_length) <= y2:
        return True
    # Test lower right corner
    if (x1 + square1_length ) >= x2 and (x1 + square1_length) <= (x2 + square2_length) and y1 >= (y2 - square2_length) and y1 <= y2:
        return True
    # Test upper right corner
    if (x1 + square1_length) >= x2 and (x1 + square1_length) <= (x2 + square2_length) and (y1 - square1_length) >= (y2 - square2_length) and (y1 - square1_length) <= y2:
        return True
    return False