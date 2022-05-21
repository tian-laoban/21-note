import sys
sys.path.append('/home/tianlaoban/.local/lib/python3.7/site-packages')
from pymouse import PyMouse
import keyboard
from time import sleep
import settings

m = PyMouse()

def up():
    x,y = m.position()
    m.move(x,y-20)

def down():
    x,y = m.position()
    m.move(x,y+20)

def left():
    x,y = m.position()
    m.move(x-20,y)

def right():
    x,y = m.position()
    m.move(x+20,y)

def left_btn():
    x,y = m.position()
    m.click(x,y,1)

def right_btn():
    x,y = m.position()
    m.click(x,y,2)


def up_left():
    pass

def up_right():
    pass

def down_left():
    pass

def down_right():
    pass


while 1:
    # start
    keyboard.wait('`+1')

    # 方向键
    keyboard.add_hotkey('0 + up',up)
    keyboard.add_hotkey('0 + down',down)
    keyboard.add_hotkey('0 + left',left)
    keyboard.add_hotkey('0 + right',right)
    # 左键，右键
    keyboard.add_hotkey('0 +1',left_btn)
    keyboard.add_hotkey('0 +2',right_btn)
    

    # end
    keyboard.wait('`+1')
    keyboard.clear_all_hotkeys()