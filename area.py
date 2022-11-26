from framework.objects.json_file_operation.access import access_point as access

def area(name: str, points: list):
        if len(points) < 3:
                print("error: not enough points for a area operation")
        else:  
                points_cord_set = [access.read(x) for x in points]
                nbCoordinates = len(points_cord_set)
                nbSegment = nbCoordinates - 1
                l = [int((points_cord_set[i+1][0] - points_cord_set[i][0]) * (points_cord_set[i+1][1] + points_cord_set[i][1])) for i in range(nbSegment)]
                print(f"The area of the shape is {abs(int(sum(l) / 2))}")