nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))


if(idade < 18):
    autorizacao = input("Os pais autorizaram a viagem? [Sim/Nao]").lower()
    

print(f"Realizando o Embarque de {nome}")