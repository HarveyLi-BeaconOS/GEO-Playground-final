class point_set:
    def __init__(self,name: str, cord: list) -> None:
        if "-" in cord:
            print("error: using undefined areas")
            return
        else:
            self.x_cord = cord[0]
            self.y_cord = cord[1]
            self.name = name
            self.points = (self.x_cord,self.y_cord)

class polygon:
    def __init__(self, name: str, *points: any) -> None:
        if "-" in points:
            print("error: using undefined areas")
            return
        else:
            first_warper = [ ]
            second_warper = [ ]
            first_warper.append(name)
            first_warper.append(points)
            second_warper.append(first_warper)
            self.name = name
            self.points = points

class segment:
    def __init__(self, name: str, *points: any) -> None:
        if "-" in points:
            print("error: using undefined areas")
            return
        else:
            first_warper = [ ]
            second_warper = [ ]
            first_warper.append(name)
            first_warper.append(points)
            second_warper.append(first_warper)
            self.name = name
            self.points = points
            print(second_warper)  