# Before running this file, snap your terminal window to the left, and your chrome browser to the right opening the course registeration page.
# Also make sure you have logged in, accept the acknowledgement and agreement.
# And finally key in your course code.

import pyautogui, sys
print('Press Ctrl-C to quit.')

# Automate clicking action
# There will be a slight pause between each click, to enable you to gain control over the program and halt it.
try:
    while True:
        # 1. 'Add Course' button
       pyautogui.click(x=1080, y=360)
       pyautogui.PAUSE = 1.5

    #    2. Click 'OK' on the alert box
       pyautogui.click(x=1200, y=180)
       pyautogui.PAUSE = 1.5

    #    3. Select Group
       pyautogui.click(x=1320, y=270)
       pyautogui.PAUSE = 1.5

    #    4. Click 'Submit'
       pyautogui.click(x=1344, y=300)
       pyautogui.PAUSE = 1.5

    #    5. Click 'OK' on "The course has reached maximum..."
       pyautogui.click(x=1200, y=306)
       pyautogui.PAUSE = 1.5

        # 6. Click on terminal for fail-safe
       pyautogui.click(x=445, y=500)
       pyautogui.PAUSE = 2
              
except KeyboardInterrupt:
    print('\n')