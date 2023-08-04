import os
from pathlib import Path


def find_screandhots():
    folder_name = "screanshots"
    path = Path(".")

    # Поиск всех папок с заданным именем в текущей директории и её поддиректориях
    folders = [folder for folder in path.glob(f"**/{folder_name}") if folder.is_dir()]

    if not folders:
        os.mkdir(os.path.join(f"{path}\pc-controller", "screanshots"))
