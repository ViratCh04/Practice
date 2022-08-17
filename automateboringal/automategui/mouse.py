import pyautogui

# the entire screen functions as a sort of cartesian system while automating, except that going down means y-coordinate increases. x still increases from left-right though

print(pyautogui.size())

width, height = pyautogui.size()
print(width, height)

print(pyautogui.position())             # tells the current position of the cursor

pyautogui.moveTo(10,50)                 # moves the cursor to specified coordinates
pyautogui.moveTo(500, 40, duration=2)      # by passing an int to the call, you can set the time it takes the cursor to reach there

pyautogui.moveRel(200, 600)               # moves the cursor by x or/and y coordinate, in relation to the current position of cursor
pyautogui.moveRel(-400, -400, duration=2) # -ve y coordinate means going up

pyautogui.click(57, 19)                     # clicks on the specified set of coordinates
pyautogui.moveRel(400, 600)
pyautogui.click()                           # feeding in the coordinates is purely optional
pyautogui.doubleClick()
pyautogui.middleClick()
pyautogui.leftClick()                       # kinda useless as click does the same

print(pyautogui.displayMousePosition())          # displays current mouse position until you hit ctrl+c. useful to note down which button is where when you want to automate
# can call this on a shell like cmd, powershell and bash too

# seems a tad more interesting than the other things shown in the course, besides regex and selenium.
# M.: look up the docs later. 