import pyautogui
import keyboard
import time

print(pyautogui.size())

while True:
    if keyboard.is_pressed('r'):
        print("Starting...")
        break

counter = 0

while counter < 50:
    if keyboard.is_pressed('s'):
        print("Ending...")
        break

    pyautogui.mouseDown(button = 'left')

    pyautogui.move(-200, -200)
    time.sleep(0.7)

    pyautogui.move(200, 0)
    time.sleep(0.7)

    pyautogui.move(200, 0)
    time.sleep(0.7)

    pyautogui.move(0, 200)
    time.sleep(0.7)

    pyautogui.move(0, 200)
    time.sleep(0.7)

    pyautogui.move(-200, 0)
    time.sleep(0.7)

    pyautogui.move(-200, 0)
    time.sleep(0.7)

    pyautogui.move(0, -200)
    time.sleep(0.7)

    pyautogui.move(200, 0)
    time.sleep(0.7)

    pyautogui.mouseUp(button = 'left')

    keyboard.press('w')
    time.sleep(0.21)
    keyboard.release('w')

    counter+= 1
