import mouse
import time


def setclicker(TaF):
    if TaF == 1:
        while True:
            mouse.click(button="left")
            time.sleep(1.11)


def Cclicker(bool):
    if bool == "on":
        # while True:
        mouse.click(button="left")
        time.sleep(1.11)
    else:
        return
