import json, os

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
