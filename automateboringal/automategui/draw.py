import pyautogui

# draws a square spiral

pyautogui.click()
distance = 200          # uses one variable to both draw out the shape and prevent infinite loop. fairly common, but should take care to not forget this while coding other things

while distance > 0:
    print(distance, 0)
    pyautogui.dragRel(distance, 0, duration=0.1)            # right
    distance -= 25
    print(0, distance)
    pyautogui.dragRel(0, distance, duration=0.1)            # down
    print(-distance, 0)
    pyautogui.dragRel(-distance, 0, duration=0.1)           # left
    distance -= 25
    print(0, -distance)
    pyautogui.dragRel(0, -distance, duration=0.1)           # up


# down and left 'drag' values are the same