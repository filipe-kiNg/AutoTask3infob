while True:
    try:
        a, b = input("Digite dois valores: ").split()

        a = int(a)
        b = int(b)

        result = a/b

        print(f"O resultado é {result}")
        break
    except ValueError:
        print("O valor ta erado")
    except ZeroDivisionError:
        print("Nao pode divider por zero")
    except Exception as e:
        print(e)
        