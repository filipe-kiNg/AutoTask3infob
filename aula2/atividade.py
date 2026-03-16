notaum= float(input("Digite a primeira nota: "))
notadois= float(input("Digite a segunda nota: "))

media = (notaum + notadois)/2

if media >=6:
    print("Aluno aporvado")
else:
    exame = float(input("digite a nota do exame fina: "))
    mediafinal = (media + exame)/2
    if mediafinal >= 6:
        print("aprovado")
    else:
        print("reporvado")