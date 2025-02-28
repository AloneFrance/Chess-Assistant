import pyautogui
import os

def screen():
    folder = "img"
    filename = os.path.join(folder, "chess.png")

    if not os.path.exists(folder):
        os.makedirs(folder)

    if os.path.exists(filename):
        os.remove(filename)

    screenshot = pyautogui.screenshot()
    screenshot.save(filename)