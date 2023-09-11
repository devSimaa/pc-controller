import os
from pathlib import Path


path = Path.cwd()

def create_folder(folder_name):

    folders = [folder for folder in path.glob(f"**/{folder_name}") if folder.is_dir()]
    if not folders:
        os.mkdir(os.path.join(f"{path}\{folder_name}"))
