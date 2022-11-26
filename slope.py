from framework.objects.json_file_operation.access import access_point as access

def slope(name: str, points: list):
    if len(points) < 2:
        print(f"error: Cannot perform a slope operation with only {len(points)} point")
    else:
        point1 = access.read(points[0])
        point2 = access.read(points[1])
        if not point1[0] - point2[0] == 0:
            slope = (point1[1] - point2[1]) / (point1[0] - point2[0])
            print(f"The slope between points {point1} and {point2} is {int(slope)}")
        else:
            print(f"The slope between points {point1} and {point2} is undefined")