import math
from framework.objects.json_file_operation.access import access_point as access

def length(points: list): # [(1,3), ()]
    length_of_sides = [int(math.sqrt((points[x-1][0] - points[x][0]) ** 2 + (points[x-1][1] - points[x][1]) ** 2))
     for x in range(len(points))]
    return length_of_sides
