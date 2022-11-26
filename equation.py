from framework.objects.json_file_operation.access import access_point as access

def equation(name: str, points: list):
    if not len(points) <= 1:
        point1 = access.read(points[0])
        point2 = access.read(points[1])
        point3 = access.read(points[2])
        if not point1[0] - point2[0] == 0:
            slope = int((point1[1] - point2[1]) / (point1[0] - point2[0]))
        else:
            slope = None
    else:
        print(f"error: Cannot construct an equation with {len(points)} point")
        return
    if not slope is None:
        intercept = int(point3[1] - slope * point3[0])
    else:
        if point1[0] == point3[0]:
            print(f"The equation of the line passing through point {point1} and {point2} is x = {point1[0]}")
        else:
            print("error(slope = None): Connot construct an equation through the points given. They may not be on the same line.")
            return
        return
    verify_y_1 = int(point3[0] * slope + intercept)
    verify_y_2 = int(point1[0] * slope + intercept)
    if verify_y_1 == point3[1] and verify_y_2 == point1[1]:
        print(f"The equation of the line passing through point {point1} and {point2} is y = {slope}x + {intercept}")
    else:
        print("error: Connot construct an equation through the points given. They may not be on the same line.")
