import pygetwindow as gw
import mouse as m
# handle = gw.getWindowsWithTitle('原神')[0]
# handle.activate()

from pynput.mouse import *
import numpy as np
from PIL import ImageGrab
import cv2
from urllib.request import urlopen
from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()
import time
time.sleep(0)
mouse = Controller()
# mouse.position = (942,111)
# mouse.click(Button.left)
import time
import pyautogui
time.sleep(1)
mouse.position = (669,255)
mouse.click(Button.left)
pyautogui.moveTo(669,255)
pyautogui.mouseDown(button='left')
pyautogui.moveTo(669,328, 1)
# time.sleep(1)
#
# # m.drag(669,255, 669,290, absolute=True, duration=0.5)
#
# time.sleep(1)
#
# mouse.press(Button.left)
# time.sleep(1)
#
# mouse.move(0, 100)
# mouse.release(Button.left)
# time.sleep(1)
#
# mouse.position = (520,410)
# mouse.click(Button.left)
# time.sleep(1)
#
# mouse.position = (640,550)
# mouse.click(Button.left)
# # mouse.position = (460,275)
# # mouse.click(Button.left)
