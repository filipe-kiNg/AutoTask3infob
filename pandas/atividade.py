import pandas as pd

sheet = pd.read_excel("pandas\\notas_estudantes.xlsx")

df_notas = pd.read_excel("pandas\\notas_estudantes.xlsx", sheet_name="Notas")
df_atividades = pd.read_excel("pandas\\notas_estudantes.xlsx", sheet_name="Atividades")

df_notas.loc[len(df_notas)] = ["Lucas silva", "Prova Final", 8.5]

df_notas.loc[(df_notas["Nome"] == "Ana Souza") & (df_notas["Atividade"] == "Trabalho 1"), "Nota"] = 9

df_notas.drop(df_notas[(df_notas["Nome"] == "Pedro Santos") & (df_notas["Atividade"] == "Prova 1")].index, inplace=True)
print(df_notas)
media = ["nome", "media"]
try:
    for nota in df_notas["Nota"]:
        if nota >= 7:
            print(nota)
except:
    print("acabou numero")

media = df_notas.groupby("Nome")["Nota"].mean()

print(df_notas[["Nome","Nota"]])

pf = df_notas
        




