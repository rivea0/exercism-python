import math

def score(x, y):
    """Return the earned points in a single toss of a Darts game."""
    distance = math.sqrt(abs(x) ** 2 + abs(y) ** 2)

    # If the point is within the bounds of specific circles
    outer = 5 < distance <= 10
    middle = 1 < distance <= 5
    inner = 0 <= distance <= 1

    scores = ((outer, 1), (middle, 5), (inner, 10))

    for i in scores:
        if i[0]:
            return i[1]

    # If the dart is outside the target
    return 0
