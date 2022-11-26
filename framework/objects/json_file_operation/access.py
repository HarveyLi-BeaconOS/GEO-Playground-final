import json,os

class write:
    def __init__(self,contents: dict) -> None:
        write.write(contents=contents, path=write.get_dir("configs/global_defined_points.json"))
    
    def get_dir(file_name: str):
        return os.getcwd() + "/" + file_name
    
    def write(contents: dict, path: str):
        with open(path, "r") as f:
            model = json.load(f)
            for i in contents:
                model[i] = contents[i]
            jsObj = json.dumps(model)
            with open(path,"w") as jsf:
                jsf.write(jsObj)

class clean:
    def __init__(self) -> None:
        clean.clean(write.get_dir("configs/global_defined_points.json"))

    def clean(path: str):
        empty_dict = { }
        with open(path, "w") as f:
            cont = json.dumps(empty_dict)
            f.write(cont)


class access_point:
    def open(path: str):
        if os.path.exists(path):
            with open(path, 'r') as file:
                return json.load(file)
        else:
            print("fatal: JavaScript Object Notation File Not Found")
            
    def read(key: str):
        try:
            return access_point.open(write.get_dir("configs/global_defined_points.json"))[key]
        except KeyError:
            print(f"error: undefined Point at {key}")

class access_shape:
    def read(key: str):
        '''Use this ONLY for polygon; to access a point, use access_point.read()'''
        coord_list = [ ]
        shape_set = access_point.open(write.get_dir("configs/global_defined_points.json"))
        try:
            shape_set[key]
        except KeyError:
            print(f"error: undefined ShapeObject at {key}")
        else:
            for x in shape_set[key][0]:
                coord_list.append(tuple(access_point.read(x)))
            return coord_list