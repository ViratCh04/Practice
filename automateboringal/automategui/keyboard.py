import pyautogui

# for focusing into the typing window
pyautogui.click(100,100);       # pick just about any coordinate where you are going to fit in the text editor
pyautogui.typewrite('Hello World!')     # types any string you pass to it
pyautogui.typewrite('Hello world!', interval=0.2)       # prints each character with the specified time interval

# pyautogui stores a string list of names for each key binding, which can be accessed by
print(pyautogui.KEYBOARD_KEYS)
pyautogui.typewrite(['a','x','right','left','left','G'], interval=0.2)

# to press a single key
pyautogui.press('f1')

# to press a key combination
pyautogui.hotkey('ctrl', 'o')