import pandas as pd

sheet = pd.read_excel("pandas\\notas_estudantes.xlsx")

df_notas = pd.read_excel("pandas\\notas_estudantes.xlsx", sheet_name="Notas")
df_atividades = pd.read_excel("pandas\\notas_estudantes.xlsx", sheet_name="Atividades")

df_notas.loc[len(df_notas)] = ["Lucas Silva", "Prova final", 8.5]

#cond = (df_notas["Nome"] == "Ana Souza") & (df_notas["Atividade"] == "Trabalho 1") 
#df_notas.loc[cond, "Nota"] = 9

#cond1 = (df_notas["Nome"] == "Pedro Santos") & (df_notas["Atividade"] == "Prova 1") 
#df_notas = df_notas[~cond1]

#f_notas = df_notas.loc[df_notas["Nota"] > 7]

#df_notas = df_notas.groupby("Nome")["Nota"].mean()

#print(df_notas[["Nome","Nota"]])

#df_notas = df_notas[df_notas["Atividade"] == "Prova Final"]

#cond = df_notas["Nota"] > 7
#print(df_notas.loc[cond,["Nome", "Atividade"]])

#df_notas.sort_values("Nome", inplace=True)

#print(df_atividades.merge(df_notas))

df_notas.to_csv("notas_estudantes_ordenado.xlsx", index=False, encoding="utf-8")

