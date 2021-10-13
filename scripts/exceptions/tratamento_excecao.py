while True:
    try:
        x = int(input("informe um numero: "))
        break
    except ValueError:
        print("numero invalido, tente novamente.")
