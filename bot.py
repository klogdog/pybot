import win32api, win32con
import ImageGrab
import os
import time
xpad = 0
ypad = 0

def screenGrab():
    box = ()
    im = ImageGrab.grab()
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')

def leftClick(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y)
    print "click"
    print x

def leftDown(x,y):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y)
    time.sleep(.1)


def leftUp(x,y):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y)
    time.sleep(.1)


def rightClick(x,y):
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y)

def rightDown(x,y):
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y)
    time.sleep(.1)

def rightUp(x,y):
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y)
    time.sleep(.1)

def getCoords():
    x,y = win32api.GetCursorPos()
    x = x - xpad
    y = y - ypad
    print x,y

def openFile():
   filepath = 'loader.bat'
   os.startfile(filepath)
   time.sleep(10)
   leftClick(1103,258)
   time.sleep(5)
   leftClick(1102,301)


def main():
  openFile()


if __name__ == '__main__':
    main()
