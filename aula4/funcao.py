def somar(a,b):
    return a + b

def imprimir(texto):
    print(texto)

def pulalinha():
    print("\n")

def ler():
    input()

imprimir("Receba")
a = ler()

imprimir("receba 2")
b = ler()

def inteiro(a,b):
    a = int(a) 
    b = int(b)

inteiro(a,b)
resposta = somar(a,b)
imprimir(f"O resultado é {resposta}")
