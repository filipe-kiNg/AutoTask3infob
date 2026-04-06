from exercicio_func import quadrado

while True:
    try:
        a = int(input("Digite um numero: "))

        result = quadrado(a)

        print(f"O quadrado de {a} é {result} ")
        break
    except Exception as e:
        print(e)