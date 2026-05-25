import pandas as pd

planilha = pd.read_excel("aula8\\sala.xltx")



planilha.loc[len(planilha), ["Nome", "Idade", "Gênero"]] = ["Gutsavo", 30, "Female"]



print(planilha)

