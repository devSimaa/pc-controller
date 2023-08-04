import pyautogui


def PKM():
    pyautogui.rightClick()


def LKM():
    pyautogui.click()


def plus_dpi(dpi):
    edit_dpi = dpi + 15
    return edit_dpi


def minus_dpi(dpi):
    edit_dpi = dpi - 15
    return edit_dpi


def mouve_x_plus(dpi):
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.moveTo(dpi + currentMouseX, currentMouseY)


def mouve_x_minus(dpi):
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.moveTo(currentMouseX - dpi, currentMouseY)


def mouve_y_plus(dpi):
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.moveTo(currentMouseX, dpi + currentMouseY)


def mouve_y_minus(dpi):
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.moveTo(currentMouseX, currentMouseY - dpi)
