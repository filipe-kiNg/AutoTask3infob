while True:
    user = input("Digite seu usuario: ")
    senha = input("Digite sua senha: ")

    if user == "admin" and senha == "admin123":
        break
    else:
        print("Usuario e ou senha invalidos")
        continue

print("Bem-vindo")