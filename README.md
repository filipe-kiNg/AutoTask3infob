## Aula 1
- Input

## Aula 2
- Condições
  - If
  - Elif
  - Else
  - Match case

## Aula 3

- Repetições
  - For
    - For em listas
    - Break
    - Continue

## Aula 4

  - While
  - Try Except
  - Funções
    - Definir funções

## Aula 5

  - Import
    - Importar funções de um outro código

## Aula 7

  - Biblioteca pyautogui
    - Como clicar na tela
      - `click`
      - `locateOnScreen`
        - `confidence`
        - `greyscale`

## Aula 8

  - Biblioteca pyautogui
    - `write`
    - `prompt`
    - `press`
    - `hotkey`

## Aula 9

  - Introdução a pandas
    - Biblioteca `pandas`
      - `loc` 
        - `df_notas = df_notas.loc[df_notas["Nota"] > 7]`
      - `read_excel`
        - `df_notas = pd.read_excel("pandas\\notas_estudantes.xlsx", sheet_name="Notas")` 
      - `groupby`
        - `df_notas = df_notas.groupby("Nome")["Nota"].mean()`
      - `to_csv`
        - `df_notas.to_csv("notas_estudantes_ordenado.xlsx", index=False, encoding="utf-8")`
      - `merge`
        - `df_atividades.merge(df_notas)`
      - `sort_values`
        - `df_notas.sort_values("Nome", inplace=True)`
    - `openpyxl`

## Bibliotecas

  - `pyautogui`
  - `pillow`
  - `opencv-python`
  - `time`
  - `pandas`