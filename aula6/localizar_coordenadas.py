import pyautogui

def mais():
    xy2 = pyautogui.locateOnScreen('aula6\\images\\+.png',confidence=0.9)
    pyautogui.click(xy2, duration=0.5, interval=0.1)

def oito():
    xy= pyautogui.locateOnScreen('aula6\\images\\8.png', confidence=0.9)
    pyautogui.click(xy, duration=0.5, interval=0.1)

def seis():
    xy3 = pyautogui.locateOnScreen('aula6\\images\\6.png',confidence=0.9)
    pyautogui.click(xy3, duration=0.5, interval=0.1)

def igual():
    xy4 = pyautogui.locateOnScreen('aula6\\images\\=.png',confidence=0.9)
    pyautogui.click(xy4, duration=0.5, interval=0.1)

oito()
mais()
seis()
igual()