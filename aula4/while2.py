#While

continuar = True

while continuar:
    aluno = input("Digite o nome do aluno: ")

    resp = int(input("Deseja continuar: \n0 pra nao \n1 pra sim: "))

    if resp  == 0:
        continuar = False
    elif resp == 1:
        continuar = True
    else:
        print("Valor invalido! Digite novamente: ")
    