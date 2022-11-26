import os

def construct_path(file_name: str) -> str:
    return os.getcwd() + f"/{file_name}"

def verify_path(path:str) -> bool:
    return os.path.exists(path)