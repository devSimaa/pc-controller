import pyautogui
import random
from pathlib import Path


# def screen():
#     path = Path(".")
#     global random_name
#     random_name = f"screenshot{random.randint(1, 20000)}.png"
#     screenshot = pyautogui.screenshot()
#     screenshot.save(f"{path}\screanshots\{random_name}")


def screen():
    global path_screan
    global random_name
    path_screan = f"{Path(__file__).parents[2]}\screanshots"
    screenshot = pyautogui.screenshot()
    random_name = f"screenshot{random.randint(1, 20000)}.png"
    screenshot.save(f"{path_screan}\{random_name}")


screen()
