import pyautogui, sys
print('Press Ctrl-C to quit.')

# Determine the location of the cursor to click. Comment the code block: Automate click action before running this block code.

try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')