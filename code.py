import win32api, win32con
import time
import quickGrab
from PIL import ImageOps

# Globals
# ------------------
x_pad = 455
y_pad = 30


def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def main():
    startGame()
    check = True
    while check:
        winVictor()
    return


def mousePos(cord):
    win32api.SetCursorPos([x_pad + cord[0], y_pad + cord[1]])


def winVictor():
    im = quickGrab.screenGrab2()
    if (im.getpixel(Cord.c_rectangle) == Color.green):
        mousePos(Cord.s_green)
        leftClick()
    if (im.getpixel(Cord.c_rectangle) == Color.magenta):
        mousePos(Cord.s_magenta)
        leftClick()
    if (im.getpixel(Cord.c_rectangle) == Color.yellow):
        mousePos(Cord.s_yellow)
        leftClick()
    if (im.getpixel(Cord.c_rectangle) == Color.blue):
        mousePos(Cord.s_blue)
        leftClick()


def get_cords():
    x, y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print(x, y)


def startGame():
    # location of first menu
    mousePos([185, 362])
    leftClick()
    time.sleep(.1)
    leftClick()


class Cord:
    s_blue = (35, 465)
    s_green = (35, 550)
    s_magenta = (335, 465)
    s_yellow = (335, 550)
    c_rectangle = (219, 440)


class Color:
    blue = (0, 130, 132)
    green = (0, 130, 0)
    magenta = (132, 0, 132)
    yellow = (132, 130, 0)


if __name__ == '__main__':
    main()
