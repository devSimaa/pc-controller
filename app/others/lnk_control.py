
from pathlib import Path



def get_file_list():
    path = Path.cwd().joinpath('lnk')

    file_list = []
    for item in path.iterdir():
        if item.is_file():
            file_list.append(item.stem) 
    return file_list

# print(get_file_list())
