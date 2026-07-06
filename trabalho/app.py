import pandas as pd
import pyautogui as pya
from time import sleep

#nao usei ia
sheet = pd.read_excel("trabalho\\clientes.xlsx")


pya.hotkey("win","d")
pya.press("win")
sleep(0.5)
pya.write("notas")
sleep(0.5)
pya.press("enter")
sleep(3)
pya.hotkey("win","up")


for index, row in sheet.iterrows():
    name = row['Nome']
    cpf = str(row['Cpf'])
    prd = row["Produto"]
    preco = str(row["Preco"])

    pya.write(name)
    pya.write(":")
    pya.press("enter")
    pya.press('tab')
    pya.write(cpf)
    pya.press("enter")
    pya.press('tab')
    pya.write(prd)
    pya.press("enter")
    pya.press('tab')
    pya.write("R$")
    pya.write(preco)
    pya.press("enter")
    
sleep(1)
pya.hotkey('ctrl',"shift",'s')
sleep(1)
pya.write("dados clientes")
sleep(1)
pya.press("enter")

    
    
  
        






