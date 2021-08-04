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


def mark_def():
    screen = np.array(ImageGrab.grab(bbox=(1240, 330, 1320, 360)))
    screen_array = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
    small_image = cv2.imread('def_main.JPG')
    main_result = cv2.matchTemplate(small_image, screen_array, method)
    main_percent, _, _, _ = cv2.minMaxLoc(main_result)
    screen = np.array(ImageGrab.grab(bbox=(1250, 500, 1340, 620)))
    screen_array = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
    small_image = cv2.imread('def.JPG')
    sub_result = cv2.matchTemplate(small_image, screen_array, method)
    sub_percent, _, _, _ = cv2.minMaxLoc(sub_result)
    if (1 - sub_percent < 0.95) and (1 - main_percent < 0.95):
        pyautogui.moveTo(1580, 465, 0)
        time.sleep(0.5)
        pyautogui.click()
        mouse.position = (x, y)


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
    n = 937
    mouse.position = (x, y)
    mouse.click(Button.left)
    for i in range(math.floor(n / 35)):
        screen = np.array(ImageGrab.grab(bbox=(350, 190, 472, 370)))
        screen_array = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
        small_image = cv2.imread('spot.JPG')
        result = cv2.matchTemplate(small_image, screen_array, method)
        mn, _, mnLoc, _ = cv2.minMaxLoc(result)
        MPx, MPy = mnLoc
        x = MPx + 350
        y = MPy + 190
        for u in range(35):
            if u != 0 and (u + 0) % 7 == 0:
                y += 140
                x = 410
            mouse.position = (x, y)
            mouse.click(Button.left)
            time.sleep(0.5)
            mark_def()
            x += 115
        for o in range(s):
            pyautogui.scroll(-1)
