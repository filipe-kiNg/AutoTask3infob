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
xy2 = pya.locateCenterOnScreen("aula7\\images\\telacheia.png", confidence=0.5)
pya.click(xy2)
sleep(1)
pya.hotkey("ctrl","shift", "n")
sleep(1)
pya.write("chatgpt.com")
sleep(1)
pya.press("enter")

sleep(2)
pya.write(pergunta)
pya.press("enter")
sleep(10)
pya.click(750, 200)
sleep(2)
pya.scroll(-10000)
try:
    xy4 = pya.locateCenterOnScreen("aula7\\images\\fechar.png",confidence=0.7)
    pya.click(xy4)
except:
    print("not found")
sleep(2)
xy3 = pya.locateCenterOnScreen("aula7\\images\\copy.png", confidence=0.9)
pya.click(xy3)

sleep(2)

pya.hotkey("alt", "tab")
sleep(1)
pya.write("gmail.com")
pya.press("enter")
sleep(2)
xy6 = pya.locateCenterOnScreen("aula7\\images\\write.png",confidence=0.9, grayscale=False)
pya.click(xy6)
sleep(2)
pya.write("pedro.alvarenga@alunos.ifsuldeminas.edu.br")
sleep(1)
pya.press("tab")
sleep(1)
pya.press("tab")
sleep(1)
pya.hotkey("ctrl","v")

