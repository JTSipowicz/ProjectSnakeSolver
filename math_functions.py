from data_structures import Rect

def compareSquares(point1, point2, rect1_length, rect2_length):
    right = point1.x + rect1_length
    top = point1.y - rect1_length
    left = point1.x
    down = point1.y
    RectA = Rect(right, top, left, down)

    right = point2.x + rect2_length
    top = point2.y - rect2_length
    left = point2.x
    down = point2.y
    RectB = Rect(right, top, left, down)

    if (RectA.left <= RectB.right and RectA.right >= RectB.left
        and RectA.top <= RectB.down and RectA.down >= RectB.top):
        return True
    else:
        return False