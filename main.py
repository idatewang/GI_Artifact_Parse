import sys
from pynput.mouse import *
import numpy as np
from PIL import ImageGrab
import cv2
from ctypes import windll
import pyautogui
import time
import math
import keyboard

user32 = windll.user32
user32.SetProcessDPIAware()
mouse = Controller()


def unlock():
    screen = np.array(ImageGrab.grab(bbox=(1560, 450, 1620, 500)))
    screen_array = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
    small_image = cv2.imread('lock.JPG')
    result = cv2.matchTemplate(small_image, screen_array, method)
    mn, _, _, _ = cv2.minMaxLoc(result)
    if 1 - mn > 0.9:
        pyautogui.moveTo(1580, 465, 0)
        time.sleep(0.5)
        pyautogui.click()
        mouse.position = (x, y)


if __name__ == "__main__":
    method = cv2.TM_SQDIFF_NORMED
    x = 410
    y = 270
    s = 49
    mouse.position = (x, y)
    mouse.click(Button.left)
    for i in range(math.floor(909 / 35)):
        screen = np.array(ImageGrab.grab(bbox=(350, 190, 472, 370)))
        screen_array = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
        small_image = cv2.imread('spot.JPG')
        result = cv2.matchTemplate(small_image, screen_array, method)
        mn, _, mnLoc, _ = cv2.minMaxLoc(result)
        MPx, MPy = mnLoc
        x = MPx + 350
        y = MPy + 190
        if keyboard.is_pressed("q"):
            sys.exit()
        for u in range(35):
            if keyboard.is_pressed("q"):
                sys.exit()
            if u != 0 and (u + 0) % 7 == 0:
                y += 140
                x = 410
            mouse.position = (x, y)
            mouse.click(Button.left)
            time.sleep(0.5)
            unlock()
            x += 115
        for o in range(s):
            pyautogui.scroll(-1)
            if keyboard.is_pressed("q"):
                sys.exit()
