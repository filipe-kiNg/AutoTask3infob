import pandas as pd
import pyautogui as pya
from time import sleep

sheet = pd.read_excel("aula12\\dados_automacao.xlsx")

for index, row in sheet.iterrows():
    name = row["nome"]
    numero = str(row["matricula"])
    curso = row["curso"]
    sexo = row["genero"]

    def fill(image, y = 0, write = None):
        campo = pya.locateCenterOnScreen(f"aula12\\images\\{image}.png", confidence=0.9)
        pya.click(campo.x, campo.y + y)
        if write:
            pya.write(write)
        pya.scroll(-90)
        sleep(1)

    try:
        fill("box")
    except:
        print("campo ja marcado")

    fill("nome",50, name)
    fill("numero",50,numero)
    fill("curso",50,curso)
    fill("M")
    fill("send")
    sleep(1)
    fill("outra")



