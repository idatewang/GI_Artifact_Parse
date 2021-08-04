import numpy as np
from PIL import ImageGrab
import cv2
from ctypes import windll
import mouse

method = cv2.TM_SQDIFF_NORMED
user32 = windll.user32
user32.SetProcessDPIAware()

screen = np.array(ImageGrab.grab(bbox=(1250, 500, 1340, 620)))
screen_array = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)

small_image = cv2.imread('def.JPG')

result = cv2.matchTemplate(small_image, screen_array, method)
mn, _, mnLoc, _ = cv2.minMaxLoc(result)

# Draw the rectangle:
# Extract the coordinates of our best match
MPx, MPy = mnLoc
print((1 - mn) * 100, MPx + 350, MPy + 190)
mouse.position = (MPx + 350, MPy + 190)
# Step 2: Get the size of the template. This is the same size as the match.
trows, tcols = small_image.shape[:2]
#
# # Step 3: Draw the rectangle on large_image
cv2.rectangle(screen_array, (MPx, MPy), (MPx + tcols, MPy + trows), (0, 0, 255), 2)

# Display the original image with the rectangle around the match.
cv2.imshow('output', screen_array)
#
# # The image is only displayed if we call this
cv2.waitKey(0)
