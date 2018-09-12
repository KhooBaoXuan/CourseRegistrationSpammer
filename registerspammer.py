# Before running this file, snap your terminal window to the left, and your chrome browser to the right opening the course registeration page.
# Also make sure you have logged in, accept the acknowledgement and agreement.
# And finally key in your course code.

import pyautogui, sys
print('Press Ctrl-C to quit.')

# Automate clicking action
try:
    while True:
        # 1. 'Add Course' button
       pyautogui.click(x=1086, y=361)
       pyautogui.PAUSE = 2

    #    2. Click 'OK' on the alert box
       pyautogui.click(x=1200, y=180)
       pyautogui.PAUSE = 2

    #    3. Select Group 4
       pyautogui.click(x=1319, y=218)
       pyautogui.PAUSE = 2

    #    4. Click 'Submit'
       pyautogui.click(x=1344, y=300)
       pyautogui.PAUSE = 2

    #    5. Click 'OK' on "The course has reached maximum..."
       pyautogui.click(x=1200, y=306)
       pyautogui.PAUSE = 2

        # 6. Click on terminal for fail-safe
       pyautogui.click(x=445, y=500)
       pyautogui.PAUSE = 2
              
except KeyboardInterrupt:
    print('\n')