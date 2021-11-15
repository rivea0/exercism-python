def equilateral(sides):
    """Check if a triangle is equilateral."""
    if 0 in sides or len(sides) != 3:
        return False
    return sides[0] == sides[1] == sides[2]
          

def isosceles(sides):
    """Check if a triangle is isosceles."""
    false_sums = (
        sides[0] + sides[1] > sides[2], 
        sides[0] + sides[2] > sides[1], 
        sides[1] + sides[2] > sides[0]
    )

    if 0 in sides or len(sides) != 3 or False in false_sums: 
        return False 

    is_it = sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2] 
    return is_it


def scalene(sides):
    """Check if a triangle is scalene."""
    false_sums = (
        sides[0] + sides[1] > sides[2], 
        sides[0] + sides[2] > sides[1], 
        sides[1] + sides[2] > sides[0]
    )

    if 0 in sides or len(sides) != 3 or False in false_sums:
        return False

    is_it = sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]
    return is_it
