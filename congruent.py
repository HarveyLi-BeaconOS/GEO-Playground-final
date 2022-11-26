import math
from framework.objects.json_file_operation.access import access_shape as access

def congruent(name: str, shape: list):
    if len(shape) < 2:
        print("error: no congruent identification operation can be performed with only one point")
    else:
        shape_1 = access.read(key=shape[0])
        shape_2 = access.read(key=shape[1])
        shape_1_side_length = [int(math.sqrt((shape_1[i][0] - shape_1[i-1][0]) ** 2 + (shape_1[i][1] - shape_1[i-1][1]) ** 2)) 
        for i in range(len(shape_1))]
        shape_2_side_length = [int(math.sqrt((shape_2[i][0] - shape_2[i-1][0]) ** 2 + (shape_2[i][1] - shape_2[i-1][1]) ** 2)) 
        for i in range(len(shape_2))]
        if len(shape_1_side_length) != len(shape_2_side_length):
            print(f"The shape defined by the point set: {shape_1} and {shape_2} is not congruent")
            return
        for x,y in zip(shape_1_side_length, shape_2_side_length):
            if x != y:
                print(f"The shape defined by the point set: {shape_1} and {shape_2} is not congruent")
                break
        else:
            print(f"The shape defined by the point set: {shape_1} and {shape_2} is congruent")