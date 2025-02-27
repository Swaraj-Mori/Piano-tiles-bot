
import pyautogui as pag
import win32api, win32con
from keyboard import is_pressed

# variables for location
x, y = [], 0
corner_1, corner_2 = (0, 0), (0, 0)

# left clicking function
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    pag.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# calculating tiles' positons before running
while corner_1 == (0, 0) or corner_2 == (0, 0):   
    if is_pressed('r'):
        if corner_1 == (0, 0):
            corner_1 = pag.position()           # upper left
            pag.sleep(1)
        else:
            corner_2 = pag.position()           # lower right


half = (corner_2[0] - corner_1[0]) // 8
for i in range(4):
    x.append(corner_1[0] + (half + half*2*i))

y = corner_1[1] + (corner_2[1] - corner_1[1])//2 

# pressing start
pag.click(x[2] + half, y)

# main loop
while not is_pressed('x'):
    for tile in x:
        if pag.pixelMatchesColor(tile, y, (0, 0, 0)):  # condition if tile appeares in one of the rows
            click(tile, y)                             # left clicking
