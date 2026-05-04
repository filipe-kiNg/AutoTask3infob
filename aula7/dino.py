import pyautogui as pya
from time import sleep

pya.hotkey("win","d")
xy = pya.locateCenterOnScreen('aula7\\images\\chrome.png', confidence=0.9, grayscale=False)
pya.doubleClick(xy, duration=0.5)
sleep(2)
xy2 = pya.locateCenterOnScreen("aula7\\images\\telacheia.png", confidence=0.5)
pya.click(xy2)
sleep(1)
pya.write("chrome://dino")
sleep(1)               
pya.press("enter")
sleep(2)

while True:
    pya.press("space")
    sleep(1)

