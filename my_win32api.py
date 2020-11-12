#-*-coding:UTF-8-*-
import win32gui,win32con,win32api
#import chardet
import time
from ctypes import *
# import itchat

#键码
VK_CODE = {
    'backspace':0x08,
    'tab':0x09,
    'clear':0x0C,
    'enter':0x0D,
    'shift':0x10,
    'ctrl':0x11,
    'alt':0x12,
    'pause':0x13,
    'caps_lock':0x14,
    'esc':0x1B,
    'spacebar':0x20,
    'page_up':0x21,
    'page_down':0x22,
    'end':0x23,
    'home':0x24,
    'left_arrow':0x25,
    'up_arrow':0x26,
    'right_arrow':0x27,
    'down_arrow':0x28,
    'select':0x29,
    'print':0x2A,
    'execute':0x2B,
    'print_screen':0x2C,
    'ins':0x2D,
    'del':0x2E,
    'help':0x2F,
    '0':0x30,
    '1':0x31,
    '2':0x32,
    '3':0x33,
    '4':0x34,
    '5':0x35,
    '6':0x36,
    '7':0x37,
    '8':0x38,
    '9':0x39,
    'a':0x41,
    'b':0x42,
    'c':0x43,
    'd':0x44,
    'e':0x45,
    'f':0x46,
    'g':0x47,
    'h':0x48,
    'i':0x49,
    'j':0x4A,
    'k':0x4B,
    'l':0x4C,
    'm':0x4D,
    'n':0x4E,
    'o':0x4F,
    'p':0x50,
    'q':0x51,
    'r':0x52,
    's':0x53,
    't':0x54,
    'u':0x55,
    'v':0x56,
    'w':0x57,
    'x':0x58,
    'y':0x59,
    'z':0x5A,
    'numpad_0':0x60,
    'numpad_1':0x61,
    'numpad_2':0x62,
    'numpad_3':0x63,
    'numpad_4':0x64,
    'numpad_5':0x65,
    'numpad_6':0x66,
    'numpad_7':0x67,
    'numpad_8':0x68,
    'numpad_9':0x69,
    'multiply_key':0x6A,
    'add_key':0x6B,
    'separator_key':0x6C,
    'subtract_key':0x6D,
    'decimal_key':0x6E,
    'divide_key':0x6F,
    'F1':0x70,
    'F2':0x71,
    'F3':0x72,
    'F4':0x73,
    'F5':0x74,
    'F6':0x75,
    'F7':0x76,
    'F8':0x77,
    'F9':0x78,
    'F10':0x79,
    'F11':0x7A,
    'F12':0x7B,
    'F13':0x7C,
    'F14':0x7D,
    'F15':0x7E,
    'F16':0x7F,
    'F17':0x80,
    'F18':0x81,
    'F19':0x82,
    'F20':0x83,
    'F21':0x84,
    'F22':0x85,
    'F23':0x86,
    'F24':0x87,
    'num_lock':0x90,
    'scroll_lock':0x91,
    'left_shift':0xA0,
    'right_shift ':0xA1,
    'left_control':0xA2,
    'right_control':0xA3,
    'left_menu':0xA4,
    'right_menu':0xA5,
    'browser_back':0xA6,
    'browser_forward':0xA7,
    'browser_refresh':0xA8,
    'browser_stop':0xA9,
    'browser_search':0xAA,
    'browser_favorites':0xAB,
    'browser_start_and_home':0xAC,
    'volume_mute':0xAD,
    'volume_Down':0xAE,
    'volume_up':0xAF,
    'next_track':0xB0,
    'previous_track':0xB1,
    'stop_media':0xB2,
    'play/pause_media':0xB3,
    'start_mail':0xB4,
    'select_media':0xB5,
    'start_application_1':0xB6,
    'start_application_2':0xB7,
    'attn_key':0xF6,
    'crsel_key':0xF7,
    'exsel_key':0xF8,
    'play_key':0xFA,
    'zoom_key':0xFB,
    'clear_key':0xFE,
    '+':0xBB,
    ',':0xBC,
    '-':0xBD,
    '.':0xBE,
    '/':0xBF,
    '`':0xC0,
    ';':0xBA,
    '[':0xDB,
    '\\':0xDC,
    ']':0xDD,
    "'":0xDE,
    '`':0xC0}

#获取位置颜色
def get_color(x, y):
    gdi32 = windll.gdi32
    user32 = windll.user32
    hdc = user32.GetDC(None)  # 获取颜色值
    pixel = gdi32.GetPixel(hdc, x, y)  # 提取RGB值
    r = pixel & 0x0000ff
    g = (pixel & 0x00ff00) >> 8
    b = pixel >> 16
    return [r, g, b]

#移动鼠标
def mouse_move(x,y):
    windll.user32.SetCursorPos(x, y)
    pass

#鼠标单击
def mouse_click(x=None,y=None):
    if not x is None and not y is None:
        mouse_move(x,y)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

#鼠标右击
def mouse_click_r(x=None,y=None):
    if not x is None and not y is None:
        mouse_move(x,y)
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

#鼠标拖动
def mouse_absolute(x,y,x1,y1):
    mouse_move(x,y) 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)    #左键按下
    # time.sleep(0.2)
    sw = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)    #获取屏幕宽度
    sh = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)    #获取屏幕高度
    mw = int(x1 * 65535 / sw) 
    mh = int(y1 * 65535 / sh)
    win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE + win32con.MOUSEEVENTF_MOVE, mw, mh, 0, 0)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

#鼠标右键拖动
def mouse_absolute_r(x,y,x1,y1):
    mouse_move(x,y) 
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)    #左键按下
    # time.sleep(0.2)
    sw = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)    #获取屏幕宽度
    sh = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)    #获取屏幕高度
    mw = int(x1 * 65535 / sw) 
    mh = int(y1 * 65535 / sh)
    win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE + win32con.MOUSEEVENTF_MOVE, mw, mh, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

#滚轮滚动
def mouse_wheel(x):
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0,x, 0)
    pass

#键盘输入字符串
def key_input_c(str=''):
    for c in str:
        win32api.keybd_event(VK_CODE[c],0,0,0)
        time.sleep(0.01)
        win32api.keybd_event(VK_CODE[c],0,win32con.KEYEVENTF_KEYUP,0)
        time.sleep(0.01)

#键盘输入功能键
def key_input_f(f=''):
    win32api.keybd_event(VK_CODE[f],0,0,0)
    time.sleep(0.01)
    win32api.keybd_event(VK_CODE[f],0,win32con.KEYEVENTF_KEYUP,0)

#键盘输入组合键
def key_input_g(k):
    if len(k) == 2:
        win32api.keybd_event(VK_CODE[k[0]],0,0,0)
        win32api.keybd_event(VK_CODE[k[1]],0,0,0)
        time.sleep(0.01)
        win32api.keybd_event(VK_CODE[k[0]],0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(VK_CODE[k[1]],0,win32con.KEYEVENTF_KEYUP,0)
    elif len(k) == 3:
        win32api.keybd_event(VK_CODE[k[0]],0,0,0)
        win32api.keybd_event(VK_CODE[k[1]],0,0,0)
        win32api.keybd_event(VK_CODE[k[2]],0,0,0)
        time.sleep(0.01)
        win32api.keybd_event(VK_CODE[k[0]],0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(VK_CODE[k[1]],0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(VK_CODE[k[2]],0,win32con.KEYEVENTF_KEYUP,0)
    else :
        return

#获取所有窗口句柄
hwnd_title = dict()
def get_all_hwnd(hwnd,mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd:win32gui.GetWindowText(hwnd)})
def  get_all_hwnd_title():
    win32gui.EnumWindows(get_all_hwnd, 0)
    return hwnd_title

#Qt自动编译_______________________________________________________________
def qt_pro():
    r1,g1,b1 =  get_color(505,914)
    if r1<230 or r1>168 :
        mouse_click(505,914)
    mouse_click_r(129,80)
    time.sleep(0.1)
    mouse_click(179,233)
    while 1:
        r,g,b = get_color(59,834)
        if((r == 80) and (g == 153)  and (b== 53)):
            time.sleep(0.1)
            mouse_click(32,948)
            return
        else:
            time.sleep(0.3)

#显示所有输出窗口
def output_win():
    print("---------------------------------")
    h_t = get_all_hwnd_title()
    for h,t in h_t.items():
        if t is not "":
            print(h, t)

#谷歌浏览器恐龙游戏脚本
def chromd_game():
    mouse_click(222,266)
    key_input_f('spacebar')
    while 1:
        r,g,b = get_color(310,545)
        if((r == 83) and (g == 83)  and (b== 83)):
            key_input_f('spacebar')
            print('1')
        if((r == 0) and (g == 0)  and (b== 0)):
            print(2)
            return
def main():
    chromd_game()
    #key_input_g(['alt','F4'])


if __name__ == '__main__':
    main()


#############################依赖环境#######################################
#1.pip install pypiwin32 取色与模拟点击 
###########################################################################

#   SetWindowPos(
# hWnd: HWND; {窗口句柄}
# hWndInsertAfter: HWND; {窗口的 Z 顺序}
# X, Y: Integer; {位置}
# cx, cy: Integer; {大小}
# uFlags: UINT {选项}
# ): BOOL;
# //hWndInsertAfter 参数可选值:
# HWND_TOP = 0; {在前面}
# HWND_BOTTOM = 1; {在后面}
# HWND_TOPMOST = HWND(-1); {在前面, 位于任何顶部窗口的前面}
# HWND_NOTOPMOST = HWND(-2); {在前面, 位于其他顶部窗口的后面}
# //uFlags 参数可选值:
# SWP_NOSIZE = 1; {忽略 cx、cy, 保持大小}
# SWP_NOMOVE = 2; {忽略 X、Y, 不改变位置}
# SWP_NOZORDER = 4; {忽略 hWndInsertAfter, 保持 Z 顺序}
# SWP_NOREDRAW = 8; {不重绘}
# SWP_NOACTIVATE = $10; {不激活}
# SWP_FRAMECHANGED = $20; {强制发送 WM_NCCALCSIZE 消息, 一般只是在改变大小时才发送此消息}
# SWP_SHOWWINDOW = $40; {显示窗口}
# SWP_HIDEWINDOW = $80; {隐藏窗口}
# SWP_NOCOPYBITS = $100; {丢弃客户区}
# SWP_NOOWNERZORDER = $200; {忽略 hWndInsertAfter, 不改变 Z 序列的所有者}
# SWP_NOSENDCHANGING = $400; {不发出 WM_WINDOWPOSCHANGING 消息}
# SWP_DRAWFRAME = SWP_FRAMECHANGED; {画边框}
# SWP_NOREPOSITION = SWP_NOOWNERZORDER;{}
# SWP_DEFERERASE = $2000; {防止产生 WM_SYNCPAINT 消息}
# SWP_ASYNCWINDOWPOS = $4000; {若调用进程不拥有窗口, 系统会向拥有窗口的线程发出需求}