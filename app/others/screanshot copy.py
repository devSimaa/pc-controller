import pyautogui
import random
from pathlib import Path
from PIL import ImageGrab

def screen():
    global path_screan, random_name
    path_screan = f"{Path(__file__).parents[2]}\screanshots"
    screenshot = ImageGrab.grab()
    random_name = f"screenshot{random.randint(1, 20000)}.png"
    screenshot.save(f"{path_screan}\{random_name}")
