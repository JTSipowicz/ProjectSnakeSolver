from data_structures import Rect

def compareSquares(x1, x2, y1, y2, rect1_length, rect2_length):
    right = x1 + rect1_length
    top = y1 - rect1_length
    left = x1
    down = y1
    RectA = Rect(right, top, left, down)

    right = x2 + rect2_length
    top = y2 - rect2_length
    left = x2
    down = y2
    RectB = Rect(right, top, left, down)
    
    if (RectA.left < RectB.right and RectA.right > RectB.left
        and RectA.top < RectB.down and RectA.down > RectB.top):
        return True
    else:
        return False