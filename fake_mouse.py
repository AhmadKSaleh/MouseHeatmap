import pyautogui as _pyautogui
class Mouse:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, x, y):
        self.x += x
        self.y += y
        return None
    def moveTo(self, x, y):
        self.x = x
        self.y = y
    def size(self):
        return _pyautogui.size()
    def position(self):
        return tuple([self.x, self.y])