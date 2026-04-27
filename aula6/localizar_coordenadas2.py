import pyautogui


xy2 = pyautogui.locateOnScreen('aula6\\images\\verde.png',confidence=0.99, grayscale=False)
pyautogui.click(xy2, duration=0.5, interval=0.1)

