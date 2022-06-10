import pyautogui



if __name__ == '__main__':
    """
    Test some functions of "pyautogui"
    """
    # My screen resolution
    print(pyautogui.size()) # Size(width=2560, height=1440)
    pyautogui.click(x=100, y=200, clicks=3, interval=1, button='right')
    pyautogui.click(clicks=2, interval=1)
    