def compareSquares(x1, x2, y1, y2, square1_length, square2_length):
    low_left1 = (x1, y1)
    low_right1 = (x1 + square1_length, y1)
    top_left1 = (x1, y1 - square1_length)
    top_right1 = (x1 + square1_length, y1 - square1_length)

    # Make Square 2 Smaller by One pixel
    low_left2 = (x2 + 1, y2 - 1)
    low_right2 = (x2 + square2_length + 1, y2 - 1)
    top_left2 = (x2 - 1, y2 - square2_length + 1)
    top_right2 = (x2 + square2_length - 1, y2 - square1_length + 1)

    if low_right1[0] >= low_left2[0] and low_left1[0] <= low_right2[0] and low_left1[1] >= (top_left2[1] - 1) and top_left1[1] <= (low_left2[1] + 1):
                    return True
    elif low_left1[0] <= low_right2[0] and low_right1[0] >= low_left2[0] and low_left1[1] >= (top_left2[1] - 1) and top_left1[1] <= (low_left2[1] + 1):
                    return True
    elif low_left1[1] >= top_left2[1] and top_left1[1] <= low_left2[1] and low_left1[0] <= (low_right2[0] + 1) and low_right1[0] >= (low_left2[0] - 1):
                    return True
    elif top_left1[1] <= low_left2[1] and low_left1[1] >= top_left2[1] and low_left1[0] <= (low_right2[0] + 1) and low_right1[0] >= (low_left2[0] - 1):
                    return True
    return False