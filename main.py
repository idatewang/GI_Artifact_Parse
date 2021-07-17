from pynput.mouse import *
import numpy as np
from PIL import ImageGrab
import cv2
from urllib.request import urlopen
from ctypes import windll

user32 = windll.user32
user32.SetProcessDPIAware()

if __name__ == "__main__":
    mouse = Controller()
    screen = np.array(ImageGrab.grab())
    screen_array = cv2.cvtColor(screen, cv2.COLOR_RGB2RGBA)
    screen_list = screen_array.tolist()
    x_coord = None
    y_coord = None

    for block_position in range(4):
        picture_urls = urlopen("https://raw.githubusercontent.com/idatewang/Automated_Piano_Tile/master/Detection%20Pictures/" + str(block_position) + ".PNG")
        image = np.array(bytearray(picture_urls.read()), dtype=np.uint8)
        image_decode = cv2.imdecode(image, -1)
        image_cv2 = np.array(image_decode)
        image_array = cv2.cvtColor(image_cv2, cv2.COLOR_RGB2RGBA)
        image_list = image_array.tolist()
        image_length = len(image_list[0])-1
        for row in range(len(screen_list)):
            if x_coord is not None and y_coord is not None:
                break
            result = all(elem in screen_list[row] for elem in image_list[15])
            if result:
                y_coord = row
                for column in range(len(screen_list[row])):
                    if screen_list[row][column] == image_list[15][0]:
                        if screen_list[row][column + image_length] == image_list[15][image_length]:
                            x_coord = column
                            break
        if x_coord is not None and y_coord is not None:
            print("Game found at block "+str(block_position)+"!")
            break

        elif x_coord is None and y_coord is None and block_position == 3:
            print("Game not found. Make sure the game board is fully exposed on the screen.")

    while True:
        game_cord = (x_coord, y_coord-90, x_coord+500, y_coord-88)
        screen = np.array(ImageGrab.grab(bbox=game_cord))
        screen = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)
        line = list(screen[0])
        if 17 in line:
            if line.index(17) == 0:  # 1
                mouse.position = (x_coord+62, y_coord+10)
                mouse.click(Button.left)
                mouse.release(Button.left)
            elif line.index(17) < 166:  # 2
                mouse.position = (x_coord+186, y_coord+10)

                mouse.click(Button.left)
                    mouse.release(Button.left)
            elif line.index(17) < 333:  # 3
                mouse.position = (x_coord+310, y_coord+10)
                mouse.click(Button.left)
                mouse.release(Button.left)
            else:  # 4
                mouse.position = (x_coord+434, y_coord+10)
                mouse.click(Button.left)
                mouse.release(Button.left)
        # else:
        #     mouse.position = (482, 622)
        #     mouse.click(Button.left)
        #     print("Restart\n")
