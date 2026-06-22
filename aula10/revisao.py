import pandas as pd

sheet = pd.read_excel("aula10\\planilha.xlsx")
#Nome, Sexo, Idade, Curso, Disciplina, Nota
sheet.loc[len(sheet)] = ["Pedro Alvarenga", "Masculino", 20, "Engenharia", "Calculo", 8]

cond = (sheet["Nome"] == "Ana Silva")
sheet.loc[cond, "Nota"] = 10


cond2 = (sheet["Nota"] < 7)
sheet = sheet.loc[~cond2]

sheet = sheet.sort_values("Nome")
qtd = sheet.value_counts("Idade")
print(sheet)
print(qtd)
