import pyautogui as pya
from time import sleep

pergunta = pya.prompt("O que voce gostaria de saber hoje:")

#pressiona um atalho do teclado
pya.hotkey("win","d")

'''
#pressiona uma tecla
pya.press("win")

#digita um texto onde o cursor está
pya.write("chrome")

pya.press("enter")
'''

xy = pya.locateCenterOnScreen('aula7\\images\\chrome.png', confidence=0.9, grayscale=False)
pya.doubleClick(xy, duration=0.5)
sleep(2)
pya.write("chatgpt.com")
sleep(1)
pya.press("enter")
sleep(2)
pya.write(pergunta)
pya.press("enter")
