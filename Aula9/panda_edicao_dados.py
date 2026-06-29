import pandas as pd

sheet = pd.read_excel("Aula9\\Dados.xlsx")

sheet.loc[16] = ["pedro", 52, 1.32, "Masculino"]



sheet.loc[16, ["Peso", "Sexo"]] = [24, "F"]

sheet.drop(5, inplace=True)

print(sheet)

