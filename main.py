from pynput.mouse import *
import numpy as np
from PIL import ImageGrab
import cv2
from urllib.request import urlopen
from ctypes import windll

user32 = windll.user32
user32.SetProcessDPIAware()
mouse = Controller()

if __name__ == "__main__":
    count = 0
    x = 0
    y = 0
    x_coord = 400
    y_coord = 270
    while count <= 979:
        mouse.position = (x_coord, y_coord)
        mouse.click(Button.left)

        if x_coord != 1120:
            x_coord += 120
        else:
            x_coord = 0
