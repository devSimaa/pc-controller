import pyautogui
import random
from pathlib import Path


def screen():
    path = Path(".")
    global random_name
    random_name = f"screenshot{random.randint(1, 20000)}.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(f"{path}\screanshots\{random_name}")


# print(Path("."))
