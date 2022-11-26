from framework.objects.json_file_operation.access import access_point as access
import length

def perimeter(name: str, points: list):
    if len(points) < 3:
        print(f"error: the primeter of the shape defined by the points set: {points} is not defined")
    else:
        shape = [access.read(key=x) for x in points]
        length_side = length.length(shape)
        print(f"The perimeter of the shape is {sum(length_side)}")